#!/usr/bin/env python3
"""Williams-Beer I_min partial information decomposition (Tier 2, DORMANT).

    *** TOY MODEL. Information-theoretic bookkeeping only. It is NOT
    *** evidence about hadronic or QCD physics and makes no physical claim.
    *** All quantities are entropies or mutual informations in bits.

    *** STATUS: DORMANT. This module is not run on the Stage 2 channel-cost
    *** tables. It stays dormant until the channel-cost line is revisited.
    *** ``__main__`` runs synthetic self-checks only and never loads
    *** channel_cost.py, procedural_share_mlpool.py, or any per-point table.

WARNING. This implements the Williams-Beer I_min decomposition
(Williams & Beer 2010). On a small set of binned continuous points
(the Stage 2 tables have 38 or 58 failure points) the atoms are
binning-sensitive: changing the number of bins, or switching
equal-width versus quantile edges, can move mass between redundancy,
unique information and synergy. Under uniform input, entropy exchange
B' equals the map entropy A0, and in the CE-6 one-bit run all four
channel costs are f-independent — they are deterministic functions of
(g, p); see docs/channel-cost-stage2.md. Williams-Beer I_min is also
known to over-count redundancy when two independent sources are copied
into the target (the two-bit COPY example: I_min assigns 1 bit of
redundancy and 1 bit of synergy, with both unique atoms zero; Harder,
Salge and Polani 2013; Bertschinger, Rauh, Olbrich, Jost and Ay 2014).

Interface (bits throughout)
---------------------------
- ``pid_williams_beer(joint)``: discrete PID of two sources S1, S2 and a
  target T from a joint pmf given as a 3-D ndarray ``p[s1, s2, t]`` or
  a dict ``{(s1, s2, t): mass}``. Masses are normalised if they do not
  already sum to 1. Returns a :class:`PIDResult`.
- ``pid_from_points(s1, s2, t, ...)``: adapter that bins per-point
  continuous arrays (intended: B', C- or C+, deficit D) into a joint
  pmf and then calls ``pid_williams_beer``. Binning is equal-width or
  quantile, with a user-chosen bin count (one integer, or a triple),
  equal-weight points or supplied non-negative weights. Deterministic:
  no RNG.

Atoms (Williams & Beer 2010). Let I(T=t; Si) = D_KL(p(Si|t) || p(Si))
be the specific information about source Si in outcome t. Then

    Red  = I_min(T; {S1, S2}) = sum_t p(t) min{I(T=t; S1), I(T=t; S2)}
    Uniq1 = I(T; S1) - Red
    Uniq2 = I(T; S2) - Red
    Syn   = I(T; S1, S2) - I(T; S1) - I(T; S2) + Red

The four atoms sum to I(T; S1, S2) and are theoretically non-negative.

Intended Stage 2 hook (not called here)::

    from channel_cost import accounting
    rows = accounting("A")["uniform"]          # or "ml"; "capacity"
    # rows[i] has keys D, Bp, Cmin, Cmax, A0, g, p, k
    pid_from_points([r["Bp"] for r in rows],
                    [r["Cmax"] for r in rows],   # or r["Cmin"]
                    [r["D"] for r in rows],
                    bins=4, method="quantile")

Run::

    python simulations/classical/pid_williams_beer.py            # synthetic self-checks
    python simulations/classical/test_pid_williams_beer.py       # or: pytest that file
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Sequence

import numpy as np

__all__ = [
    "PIDResult",
    "BinnedJoint",
    "pid_williams_beer",
    "pid_from_points",
    "discretise_to_joint",
    "example_joint",
    "EXAMPLE_ATOMS",
    "shannon",
]


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PIDResult:
    """Williams-Beer I_min atoms and the mutual informations they come from.

    All fields are in bits. ``redundancy + unique1 + unique2 + synergy``
    equals ``I_T_S12`` (= I(T; S1, S2)) up to rounding.
    """

    redundancy: float
    unique1: float
    unique2: float
    synergy: float
    I_T_S1: float
    I_T_S2: float
    I_T_S12: float
    H_T: float
    H_S1: float
    H_S2: float
    H_S12: float

    def atoms(self) -> tuple[float, float, float, float]:
        """(redundancy, unique1, unique2, synergy)."""
        return (self.redundancy, self.unique1, self.unique2, self.synergy)

    def atoms_sum(self) -> float:
        return float(sum(self.atoms()))


@dataclass(frozen=True)
class BinnedJoint:
    """Joint pmf produced by :func:`discretise_to_joint`.

    ``joint[i, j, k]`` is the probability of (S1 bin i, S2 bin j, T bin k).
    ``n_bins`` is the effective bin count after merging duplicate edges
    (quantile binning on data with few unique values can yield fewer bins
    than requested). ``indices`` has shape (n_points, 3).
    """

    joint: np.ndarray
    edges: tuple[np.ndarray, np.ndarray, np.ndarray]
    indices: np.ndarray
    n_bins: tuple[int, int, int]
    method: str
    weights: np.ndarray
    # requested bin counts before merging duplicate edges
    requested_bins: tuple[int, int, int] = field(default=(0, 0, 0))


# ---------------------------------------------------------------------------
# Entropy helpers (bits)
# ---------------------------------------------------------------------------

def _xlog2x(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    out = np.zeros_like(p)
    mask = p > 0.0
    out[mask] = p[mask] * np.log2(p[mask])
    return out


def shannon(p: ArrayLike) -> float:
    """Shannon entropy of a discrete distribution, in bits.

    ``p`` is treated as a mass vector (flattened). Non-positive entries
    are ignored. If the masses do not sum to 1 they are renormalised.
    The zero distribution has entropy 0.
    """
    p = np.asarray(p, dtype=float).ravel()
    p = p[p > 0.0]
    total = float(p.sum())
    if total <= 0.0:
        return 0.0
    p = p / total
    return float(-_xlog2x(p).sum())


ArrayLike = Any  # numpy-compatible; kept loose so lists are accepted


def _kl_bits(p: np.ndarray, q: np.ndarray) -> float:
    """D_KL(p || q) in bits. Support of p must lie in support of q."""
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    mask = p > 0.0
    if not np.all(q[mask] > 0.0):
        return float("inf")
    return float(np.sum(p[mask] * (np.log2(p[mask]) - np.log2(q[mask]))))


def _mutual_info(p_xy: np.ndarray) -> float:
    """I(X; Y) from a 2-D joint, in bits. The joint is renormalised."""
    p = np.asarray(p_xy, dtype=float)
    total = float(p.sum())
    if total <= 0.0:
        return 0.0
    p = p / total
    return shannon(p.sum(axis=1)) + shannon(p.sum(axis=0)) - shannon(p)


# ---------------------------------------------------------------------------
# Joint normalisation
# ---------------------------------------------------------------------------

def _joint_from_dict(
    joint: Mapping[tuple[Any, Any, Any], float],
) -> tuple[np.ndarray, tuple[list, list, list]]:
    if not joint:
        raise ValueError("empty joint")
    s1_lv = _sorted_levels(k[0] for k in joint)
    s2_lv = _sorted_levels(k[1] for k in joint)
    t_lv = _sorted_levels(k[2] for k in joint)
    i1 = {v: i for i, v in enumerate(s1_lv)}
    i2 = {v: i for i, v in enumerate(s2_lv)}
    it = {v: i for i, v in enumerate(t_lv)}
    p = np.zeros((len(s1_lv), len(s2_lv), len(t_lv)), dtype=float)
    for key, mass in joint.items():
        if not isinstance(key, tuple) or len(key) != 3:
            raise ValueError(f"joint dict keys must be (s1, s2, t) tuples; got {key!r}")
        p[i1[key[0]], i2[key[1]], it[key[2]]] += float(mass)
    return p, (s1_lv, s2_lv, t_lv)


def _sorted_levels(values: Iterable[Any]) -> list:
    uniq = list(dict.fromkeys(values))
    try:
        return sorted(uniq)
    except TypeError:
        return sorted(uniq, key=lambda x: (str(type(x).__name__), repr(x)))


def _as_joint(joint: ArrayLike | Mapping) -> np.ndarray:
    if isinstance(joint, Mapping):
        p, _ = _joint_from_dict(joint)
    else:
        p = np.asarray(joint, dtype=float)
        if p.ndim != 3:
            raise ValueError(
                f"joint array must be 3-D with axes (S1, S2, T); got shape {p.shape}"
            )
    if not np.all(np.isfinite(p)):
        raise ValueError("joint contains NaN or Inf")
    if np.any(p < 0.0):
        raise ValueError("joint contains negative masses")
    total = float(p.sum())
    if total <= 0.0:
        raise ValueError("joint has zero total mass")
    return p / total


# ---------------------------------------------------------------------------
# Discrete Williams-Beer PID
# ---------------------------------------------------------------------------

def pid_williams_beer(joint: ArrayLike | Mapping) -> PIDResult:
    """Williams-Beer I_min PID of two sources S1, S2 and target T, in bits.

    Parameters
    ----------
    joint :
        A 3-D ndarray ``p[s1, s2, t]``, or a dict mapping ``(s1, s2, t)``
        to a non-negative mass. Masses are renormalised to a pmf.

    Returns
    -------
    PIDResult
        Atoms ``redundancy`` (I_min), ``unique1``, ``unique2``,
        ``synergy``, plus I(T; S1), I(T; S2), I(T; S1, S2) and the
        Shannon entropies of T, S1, S2 and (S1, S2). Units: bits.

    Notes
    -----
    See the module docstring for the I_min formulae, the binning
    warning, the CE-6 f-independence caveat, and the known I_min
    over-count of redundancy on the independent-source COPY gate.
    """
    p = _as_joint(joint)
    p_s1s2 = p.sum(axis=2)
    p_s1t = p.sum(axis=1)
    p_s2t = p.sum(axis=0)
    p_s1 = p_s1t.sum(axis=1)
    p_s2 = p_s2t.sum(axis=1)
    p_t = p_s1t.sum(axis=0)

    h_t = shannon(p_t)
    h_s1 = shannon(p_s1)
    h_s2 = shannon(p_s2)
    h_s12 = shannon(p_s1s2)
    i_t_s1 = _mutual_info(p_s1t)
    i_t_s2 = _mutual_info(p_s2t)
    i_t_s12 = h_t + h_s12 - shannon(p)  # I(T; S1, S2)

    red = 0.0
    for t, pt in enumerate(p_t):
        if pt <= 0.0:
            continue
        # p(S1 | T=t) and p(S2 | T=t)
        cond1 = p_s1t[:, t] / pt
        cond2 = p_s2t[:, t] / pt
        spec1 = _kl_bits(cond1, p_s1)
        spec2 = _kl_bits(cond2, p_s2)
        red += float(pt) * min(spec1, spec2)

    uniq1 = i_t_s1 - red
    uniq2 = i_t_s2 - red
    syn = i_t_s12 - i_t_s1 - i_t_s2 + red
    return PIDResult(
        redundancy=float(red),
        unique1=float(uniq1),
        unique2=float(uniq2),
        synergy=float(syn),
        I_T_S1=float(i_t_s1),
        I_T_S2=float(i_t_s2),
        I_T_S12=float(i_t_s12),
        H_T=float(h_t),
        H_S1=float(h_s1),
        H_S2=float(h_s2),
        H_S12=float(h_s12),
    )


# ---------------------------------------------------------------------------
# Adapter: continuous per-point arrays -> binned joint -> PID
# ---------------------------------------------------------------------------

_METHODS = ("equal-width", "quantile")


def _as_bins(bins: int | Sequence[int]) -> tuple[int, int, int]:
    if isinstance(bins, (int, np.integer)):
        n = int(bins)
        if n < 1:
            raise ValueError(f"bins must be >= 1; got {n}")
        return (n, n, n)
    seq = tuple(int(b) for b in bins)
    if len(seq) != 3 or any(b < 1 for b in seq):
        raise ValueError(f"bins must be an int or a triple of ints >= 1; got {bins!r}")
    return seq  # type: ignore[return-value]


def _edges_equal_width(x: np.ndarray, n_bins: int) -> np.ndarray:
    lo = float(np.min(x))
    hi = float(np.max(x))
    if hi <= lo:
        # One bin around the constant; width 1 is conventional only.
        return np.array([lo - 0.5, lo + 0.5], dtype=float)
    return np.linspace(lo, hi, n_bins + 1, dtype=float)


def _edges_quantile(x: np.ndarray, n_bins: int) -> np.ndarray:
    # Deterministic: numpy default linear quantiles, no RNG.
    qs = np.linspace(0.0, 1.0, n_bins + 1)
    edges = np.quantile(x, qs, method="linear")
    edges = np.unique(np.asarray(edges, dtype=float))
    if edges.size == 1:
        v = float(edges[0])
        return np.array([v - 0.5, v + 0.5], dtype=float)
    return edges


def _assign(x: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """Bin index in 0..n_bins-1. The last bin is closed on the right."""
    # searchsorted side='right' on interior edges: x==hi goes into the last bin.
    idx = np.searchsorted(edges, x, side="right") - 1
    return np.clip(idx, 0, len(edges) - 2).astype(int)


def discretise_to_joint(
    s1: ArrayLike,
    s2: ArrayLike,
    t: ArrayLike,
    *,
    bins: int | Sequence[int] = 4,
    method: str = "equal-width",
    weights: ArrayLike | None = None,
) -> BinnedJoint:
    """Bin three aligned per-point arrays into a joint pmf on the bin indices.

    Parameters
    ----------
    s1, s2, t :
        1-D arrays of the same length (one entry per point). Intended
        sources / target for the Stage 2 adapter: entropy exchange B',
        complementary-channel entropy C- or C+, and the deficit D.
        The arrays may be continuous; they are not assumed to be
        pre-binned.
    bins :
        Either a single integer (the same requested bin count for all
        three variables) or a triple ``(n_s1, n_s2, n_t)``. Must be
        >= 1. The effective count can be smaller if quantile edges
        collide (constant or few-valued data).
    method :
        ``"equal-width"``: edges are ``linspace(min, max, n+1)``. If
        ``min == max``, a single bin of width 1 is used.
        ``"quantile"``: edges are the linear quantiles at
        ``0, 1/n, ..., 1``; duplicate edges are merged. Deterministic;
        uses ``numpy.quantile(..., method="linear")``.
    weights :
        Optional non-negative masses of length n. Default: every point
        has weight 1 (equal-weight empirical measure). Weights are
        renormalised to a pmf.

    Returns
    -------
    BinnedJoint
        Normalised 3-D joint, edges, per-point bin indices, and the
        effective bin counts.

    Notes
    -----
    Assignment uses ``searchsorted(..., side="right")`` so that the
    maximum value falls in the last bin (the last bin is closed). The
    map from points to the joint is deterministic: no RNG, and the
    result does not depend on point order when weights travel with the
    points (the joint is a histogram).
    """
    if method not in _METHODS:
        raise ValueError(f"method must be one of {_METHODS}; got {method!r}")
    x1 = np.asarray(s1, dtype=float).ravel()
    x2 = np.asarray(s2, dtype=float).ravel()
    xt = np.asarray(t, dtype=float).ravel()
    n = x1.size
    if x2.size != n or xt.size != n:
        raise ValueError(
            f"s1, s2, t must have the same length; got {x1.size}, {x2.size}, {xt.size}"
        )
    if n == 0:
        raise ValueError("s1, s2, t are empty")
    for name, arr in (("s1", x1), ("s2", x2), ("t", xt)):
        if not np.all(np.isfinite(arr)):
            raise ValueError(f"{name} contains NaN or Inf")

    if weights is None:
        w = np.ones(n, dtype=float)
    else:
        w = np.asarray(weights, dtype=float).ravel()
        if w.size != n:
            raise ValueError(f"weights must have length {n}; got {w.size}")
        if not np.all(np.isfinite(w)) or np.any(w < 0.0):
            raise ValueError("weights must be finite and non-negative")
        if float(w.sum()) <= 0.0:
            raise ValueError("weights have zero total mass")

    req = _as_bins(bins)
    edge_fn = _edges_equal_width if method == "equal-width" else _edges_quantile
    edges = tuple(edge_fn(arr, n_req) for arr, n_req in zip((x1, x2, xt), req))
    idx = np.column_stack([_assign(arr, ed) for arr, ed in zip((x1, x2, xt), edges)])
    n_eff = tuple(int(ed.size - 1) for ed in edges)
    joint = np.zeros(n_eff, dtype=float)
    # Add at the (bin1, bin2, t-bin) of each point.
    np.add.at(joint, (idx[:, 0], idx[:, 1], idx[:, 2]), w)
    joint = joint / joint.sum()
    return BinnedJoint(
        joint=joint,
        edges=edges,  # type: ignore[arg-type]
        indices=idx,
        n_bins=n_eff,  # type: ignore[arg-type]
        method=method,
        weights=w,
        requested_bins=req,
    )


def pid_from_points(
    s1: ArrayLike,
    s2: ArrayLike,
    t: ArrayLike,
    *,
    bins: int | Sequence[int] = 4,
    method: str = "equal-width",
    weights: ArrayLike | None = None,
) -> tuple[PIDResult, BinnedJoint]:
    """Discretise per-point (S1, S2, T) arrays and return the I_min PID.

    Wrapper around :func:`discretise_to_joint` followed by
    :func:`pid_williams_beer`. See those functions and the module
    docstring for binning rules, units (bits), the binning-sensitivity
    warning on 38/58-point tables, and the CE-6 f-independence caveat.
    This function does not load Stage 2 data; the caller would pass
    arrays such as B', C± and D.

    Returns
    -------
    (PIDResult, BinnedJoint)
    """
    binned = discretise_to_joint(
        s1, s2, t, bins=bins, method=method, weights=weights
    )
    return pid_williams_beer(binned.joint), binned


# ---------------------------------------------------------------------------
# Named synthetic joints (self-checks and tests; not Stage 2 data)
# ---------------------------------------------------------------------------

# Documented Williams-Beer values, in bits, for the joints below.
# AND redundancy is I(T; S1) = h2(1/4) - 1/2 = 1.5 - 0.75 log2(3)
#   ≈ 0.311278124459, and synergy is exactly 1/2.
# COPY (two-bit copy, T = (S1, S2), S1 ⊥ S2 fair): I_min gives
#   redundancy = 1, unique1 = unique2 = 0, synergy = 1. That assignment
#   of a bit of redundancy (and a bit of synergy) to two independent
#   copied sources is the known I_min over-count (Harder et al. 2013;
#   Bertschinger et al. 2014).
_AND_RED = 1.5 - 0.75 * float(np.log2(3.0))

EXAMPLE_ATOMS: dict[str, tuple[float, float, float, float]] = {
    # name: (redundancy, unique1, unique2, synergy)
    "xor": (0.0, 0.0, 0.0, 1.0),
    "and": (_AND_RED, 0.0, 0.0, 0.5),
    "copy": (1.0, 0.0, 0.0, 1.0),
    "rdn": (1.0, 0.0, 0.0, 0.0),
    "unq": (0.0, 1.0, 0.0, 0.0),
}


def example_joint(name: str) -> np.ndarray:
    """Return a normalised 3-D joint for a named synthetic gate.

    All sources are fair bits unless noted. Target encoding for COPY:
    ``T = 2*S1 + S2`` (four values). UNQ: ``T = S1``, with S2 an
    independent unused fair bit.

    ======== =============================================
    name     Williams-Beer atoms (R, U1, U2, S), bits
    ======== =============================================
    ``xor``  (0, 0, 0, 1)
    ``and``  (h2(1/4)-1/2, 0, 0, 1/2)  ≈ (0.311278, 0, 0, 0.5)
    ``copy`` (1, 0, 0, 1)   two-bit copy; I_min over-count
    ``rdn``  (1, 0, 0, 0)   S1 = S2 = T
    ``unq``  (0, 1, 0, 0)   T = S1, S2 independent
    ======== =============================================

    Values are also in :data:`EXAMPLE_ATOMS`.
    """
    key = name.strip().lower()
    if key == "xor":
        # T = S1 XOR S2; four equally likely atoms.
        p = np.zeros((2, 2, 2))
        p[0, 0, 0] = p[0, 1, 1] = p[1, 0, 1] = p[1, 1, 0] = 0.25
        return p
    if key == "and":
        p = np.zeros((2, 2, 2))
        p[0, 0, 0] = p[0, 1, 0] = p[1, 0, 0] = p[1, 1, 1] = 0.25
        return p
    if key == "copy":
        # Two-bit copy: T encodes (S1, S2). I(T; S1)=I(T; S2)=1, I(T;S1,S2)=2.
        p = np.zeros((2, 2, 4))
        for a in (0, 1):
            for b in (0, 1):
                p[a, b, 2 * a + b] = 0.25
        return p
    if key == "rdn":
        p = np.zeros((2, 2, 2))
        p[0, 0, 0] = p[1, 1, 1] = 0.5
        return p
    if key == "unq":
        p = np.zeros((2, 2, 2))
        # T = S1; S2 independent fair and unused.
        p[0, 0, 0] = p[0, 1, 0] = p[1, 0, 1] = p[1, 1, 1] = 0.25
        return p
    raise KeyError(f"unknown example joint {name!r}; expected one of {sorted(EXAMPLE_ATOMS)}")


# ---------------------------------------------------------------------------
# Synthetic self-checks (the only __main__ path; no Stage 2 data)
# ---------------------------------------------------------------------------

_ATOL = 1e-12


def _close(a: float, b: float, atol: float = _ATOL) -> bool:
    return abs(float(a) - float(b)) <= atol


def self_checks() -> list[str]:
    """Run synthetic gate and invariance checks. Raises on failure."""
    lines: list[str] = []
    for name, expected in EXAMPLE_ATOMS.items():
        r = pid_williams_beer(example_joint(name))
        got = r.atoms()
        if not all(_close(g, e) for g, e in zip(got, expected)):
            raise AssertionError(f"{name}: got {got}, expected {expected}")
        if not _close(r.atoms_sum(), r.I_T_S12):
            raise AssertionError(f"{name}: atoms sum {r.atoms_sum()} != I(T;S1,S2) {r.I_T_S12}")
        lines.append(
            f"{name}: R={r.redundancy:.12f} U1={r.unique1:.12f} "
            f"U2={r.unique2:.12f} S={r.synergy:.12f} (matches documented WB values)"
        )

    # Dict input agrees with the ndarray form (XOR).
    xor_dict = {(0, 0, 0): 1, (0, 1, 1): 1, (1, 0, 1): 1, (1, 1, 0): 1}  # unnormalised
    r_dict = pid_williams_beer(xor_dict)
    r_arr = pid_williams_beer(example_joint("xor"))
    if any(not _close(a, b) for a, b in zip(r_dict.atoms(), r_arr.atoms())):
        raise AssertionError("dict and ndarray XOR joints disagree")
    lines.append("dict vs ndarray (XOR): agree")

    # Adapter recovers XOR when the already-discrete bits are equal-width binned.
    pts = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=float)
    r_ad, binned = pid_from_points(
        pts[:, 0], pts[:, 1], pts[:, 2], bins=2, method="equal-width"
    )
    if any(not _close(a, b) for a, b in zip(r_ad.atoms(), EXAMPLE_ATOMS["xor"])):
        raise AssertionError(f"adapter XOR recovery failed: {r_ad.atoms()}")
    lines.append(f"adapter equal-width bins=2 recovers XOR (n_bins={binned.n_bins})")

    # Adapter determinism: same points, same result; weights vs repetition.
    rng = np.random.default_rng(0)  # local to the self-check, not a data path
    s1, s2, t = rng.normal(size=(3, 40))
    a1, b1 = pid_from_points(s1, s2, t, bins=3, method="quantile")
    a2, b2 = pid_from_points(s1, s2, t, bins=3, method="quantile")
    if not np.allclose(b1.joint, b2.joint) or any(
        not _close(x, y) for x, y in zip(a1.atoms(), a2.atoms())
    ):
        raise AssertionError("adapter is not deterministic")
    # Doubling a point's weight equals appending a duplicate with unit weights.
    w = np.ones(40)
    w[0] = 2.0
    r_w, _ = pid_from_points(s1, s2, t, bins=3, method="equal-width", weights=w)
    r_dup, _ = pid_from_points(
        np.r_[s1, s1[:1]], np.r_[s2, s2[:1]], np.r_[t, t[:1]],
        bins=3, method="equal-width",
    )
    if any(not _close(x, y) for x, y in zip(r_w.atoms(), r_dup.atoms())):
        raise AssertionError("weighted point != duplicated point")
    lines.append("adapter determinism and weight=duplication: OK")

    # Non-negativity and atoms-sum on random dense pmfs (fixed seed).
    for shape in ((2, 2, 2), (3, 2, 4), (2, 5, 3)):
        raw = rng.random(shape)
        raw = raw / raw.sum()
        r = pid_williams_beer(raw)
        if any(x < -1e-10 for x in r.atoms()):
            raise AssertionError(f"negative atom on random pmf {shape}: {r.atoms()}")
        if not _close(r.atoms_sum(), r.I_T_S12, atol=1e-10):
            raise AssertionError(f"atoms sum failed on {shape}")
    lines.append("random pmfs: atoms non-negative and sum to I(T;S1,S2)")
    return lines


def main(argv: list[str] | None = None) -> int:
    """Synthetic self-checks only. No Stage 2 tables are loaded."""
    ap = argparse.ArgumentParser(
        description=(
            "Williams-Beer I_min PID (DORMANT). Runs synthetic self-checks only; "
            "does not load Stage 2 channel-cost data."
        )
    )
    ap.add_argument(
        "--check",
        action="store_true",
        help="same as the default: run synthetic self-checks and exit",
    )
    ap.parse_args(argv)
    print("TOY MODEL (Tier 2). Information-theoretic bookkeeping only;")
    print("NOT evidence about hadronic or QCD physics; no physical claim.")
    print("STATUS: DORMANT. Synthetic self-checks only; no Stage 2 data loaded.\n")
    for line in self_checks():
        print("check: " + line)
    print("\nAll synthetic self-checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
