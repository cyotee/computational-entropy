"""Pytest for simulations/classical/pid_williams_beer.py (synthetic data only).

These tests never load Stage 2 tables, channel_cost.py, or the ML pool.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

_MOD = Path(__file__).resolve().parent / "pid_williams_beer.py"
_spec = importlib.util.spec_from_file_location("pid_williams_beer", _MOD)
assert _spec and _spec.loader
import sys
_pid = importlib.util.module_from_spec(_spec)
sys.modules["pid_williams_beer"] = _pid  # required before exec; dataclasses look it up
_spec.loader.exec_module(_pid)

EXAMPLE_ATOMS = _pid.EXAMPLE_ATOMS
discretise_to_joint = _pid.discretise_to_joint
example_joint = _pid.example_joint
pid_from_points = _pid.pid_from_points
pid_williams_beer = _pid.pid_williams_beer
self_checks = _pid.self_checks
shannon = _pid.shannon

ATOL = 1e-10


def _atoms(name: str):
    return pid_williams_beer(example_joint(name))


@pytest.mark.parametrize("name", sorted(EXAMPLE_ATOMS))
def test_documented_gate_atoms(name: str) -> None:
    r = _atoms(name)
    expected = EXAMPLE_ATOMS[name]
    assert r.atoms() == pytest.approx(expected, abs=ATOL)
    assert r.atoms_sum() == pytest.approx(r.I_T_S12, abs=ATOL)


def test_xor_synergy_one_others_zero() -> None:
    r = _atoms("xor")
    assert r.synergy == pytest.approx(1.0, abs=ATOL)
    assert r.redundancy == pytest.approx(0.0, abs=ATOL)
    assert r.unique1 == pytest.approx(0.0, abs=ATOL)
    assert r.unique2 == pytest.approx(0.0, abs=ATOL)
    assert r.I_T_S12 == pytest.approx(1.0, abs=ATOL)
    assert r.I_T_S1 == pytest.approx(0.0, abs=ATOL)
    assert r.I_T_S2 == pytest.approx(0.0, abs=ATOL)


def test_and_redundancy_and_synergy() -> None:
    # Documented WB values: Red = I(T; S1) = h2(1/4) - 1/2, Syn = 1/2, Uniq = 0.
    h2_quarter = shannon([0.25, 0.75])
    red = h2_quarter - 0.5
    assert red == pytest.approx(0.311278124459, abs=1e-12)
    r = _atoms("and")
    assert r.redundancy == pytest.approx(red, abs=ATOL)
    assert r.redundancy == pytest.approx(0.311278124459, abs=1e-9)
    assert r.synergy == pytest.approx(0.5, abs=ATOL)
    assert r.unique1 == pytest.approx(0.0, abs=ATOL)
    assert r.unique2 == pytest.approx(0.0, abs=ATOL)
    assert r.I_T_S1 == pytest.approx(red, abs=ATOL)
    assert r.I_T_S2 == pytest.approx(red, abs=ATOL)
    assert r.I_T_S12 == pytest.approx(h2_quarter, abs=ATOL)


def test_copy_two_bit_documented_wb_values() -> None:
    """Two-bit copy: T = (S1, S2), S1 ⊥ S2 fair.

    Williams-Beer I_min assigns R=1, U1=U2=0, S=1. This is the known
    over-count of redundancy for independent sources (Harder et al. 2013;
    Bertschinger et al. 2014). The test asserts those documented WB
    values, not an independent-source intuition (which would want
    R=0, U1=U2=1, S=0).
    """
    r = _atoms("copy")
    assert r.redundancy == pytest.approx(1.0, abs=ATOL)
    assert r.unique1 == pytest.approx(0.0, abs=ATOL)
    assert r.unique2 == pytest.approx(0.0, abs=ATOL)
    assert r.synergy == pytest.approx(1.0, abs=ATOL)
    assert r.I_T_S1 == pytest.approx(1.0, abs=ATOL)
    assert r.I_T_S2 == pytest.approx(1.0, abs=ATOL)
    assert r.I_T_S12 == pytest.approx(2.0, abs=ATOL)
    assert r.H_T == pytest.approx(2.0, abs=ATOL)


def test_rdn_redundancy_one() -> None:
    r = _atoms("rdn")
    assert r.redundancy == pytest.approx(1.0, abs=ATOL)
    assert r.unique1 == pytest.approx(0.0, abs=ATOL)
    assert r.unique2 == pytest.approx(0.0, abs=ATOL)
    assert r.synergy == pytest.approx(0.0, abs=ATOL)
    assert r.I_T_S12 == pytest.approx(1.0, abs=ATOL)


def test_unq_unique1_one() -> None:
    r = _atoms("unq")
    assert r.unique1 == pytest.approx(1.0, abs=ATOL)
    assert r.unique2 == pytest.approx(0.0, abs=ATOL)
    assert r.redundancy == pytest.approx(0.0, abs=ATOL)
    assert r.synergy == pytest.approx(0.0, abs=ATOL)
    assert r.I_T_S1 == pytest.approx(1.0, abs=ATOL)
    assert r.I_T_S2 == pytest.approx(0.0, abs=ATOL)
    assert r.I_T_S12 == pytest.approx(1.0, abs=ATOL)


def test_dict_and_array_agree_on_xor() -> None:
    # Unnormalised dict masses.
    d = {(0, 0, 0): 2.0, (0, 1, 1): 2.0, (1, 0, 1): 2.0, (1, 1, 0): 2.0}
    r_d = pid_williams_beer(d)
    r_a = pid_williams_beer(example_joint("xor"))
    assert r_d.atoms() == pytest.approx(r_a.atoms(), abs=ATOL)


@pytest.mark.parametrize("shape", [(2, 2, 2), (3, 2, 4), (2, 5, 3), (4, 3, 5)])
def test_random_pmfs_nonnegative_and_atoms_sum(shape: tuple[int, int, int]) -> None:
    rng = np.random.default_rng(2026 + shape[0] + 10 * shape[1] + 100 * shape[2])
    p = rng.random(shape)
    p = p / p.sum()
    r = pid_williams_beer(p)
    for atom in r.atoms():
        assert atom >= -1e-10, r.atoms()
    assert r.atoms_sum() == pytest.approx(r.I_T_S12, abs=1e-10)


def test_adapter_recovers_xor_from_discrete_points() -> None:
    pts = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=float)
    r, binned = pid_from_points(pts[:, 0], pts[:, 1], pts[:, 2], bins=2, method="equal-width")
    assert r.atoms() == pytest.approx(EXAMPLE_ATOMS["xor"], abs=ATOL)
    assert binned.n_bins == (2, 2, 2)
    assert binned.method == "equal-width"


def test_adapter_binning_determinism() -> None:
    rng = np.random.default_rng(7)
    s1, s2, t = rng.normal(size=(3, 58))  # length is the Stage 2 58-point count
    for method in ("equal-width", "quantile"):
        r1, b1 = pid_from_points(s1, s2, t, bins=5, method=method)
        r2, b2 = pid_from_points(s1, s2, t, bins=5, method=method)
        assert np.allclose(b1.joint, b2.joint)
        assert np.array_equal(b1.indices, b2.indices)
        for e, f in zip(b1.edges, b2.edges):
            assert np.allclose(e, f)
        assert r1.atoms() == pytest.approx(r2.atoms(), abs=0.0)
        # Permuting points with unit weights leaves the joint unchanged.
        perm = rng.permutation(58)
        _, bp = pid_from_points(s1[perm], s2[perm], t[perm], bins=5, method=method)
        assert np.allclose(b1.joint, bp.joint)


def test_adapter_weights_equal_duplication() -> None:
    rng = np.random.default_rng(11)
    s1, s2, t = rng.normal(size=(3, 20))
    w = np.ones(20)
    w[3] = 2.0
    r_w, b_w = pid_from_points(s1, s2, t, bins=4, method="equal-width", weights=w)
    r_d, b_d = pid_from_points(
        np.r_[s1, s1[3:4]],
        np.r_[s2, s2[3:4]],
        np.r_[t, t[3:4]],
        bins=4,
        method="equal-width",
    )
    assert np.allclose(b_w.joint, b_d.joint)
    assert r_w.atoms() == pytest.approx(r_d.atoms(), abs=ATOL)


def test_adapter_per_variable_bins_and_constant_column() -> None:
    s1 = np.array([0.0, 0.5, 1.0, 1.5])
    s2 = np.zeros(4)  # constant: effective 1 bin
    t = np.array([0.0, 1.0, 2.0, 3.0])
    b = discretise_to_joint(s1, s2, t, bins=(4, 8, 4), method="equal-width")
    assert b.n_bins[0] == 4
    assert b.n_bins[1] == 1
    assert b.n_bins[2] == 4
    assert b.requested_bins == (4, 8, 4)
    assert b.joint.shape == (4, 1, 4)
    assert b.joint.sum() == pytest.approx(1.0, abs=ATOL)


def test_quantile_merges_duplicate_edges() -> None:
    # Two distinct values, fair XOR (four equally likely points). Requested
    # 8 quantile bins collapse below 8 once duplicate linear-quantile edges
    # are merged; 0 and 1 still land in different bins, so XOR is recovered.
    s1 = np.array([0.0, 0.0, 1.0, 1.0])
    s2 = np.array([0.0, 1.0, 0.0, 1.0])
    t = np.array([0.0, 1.0, 1.0, 0.0])
    b = discretise_to_joint(s1, s2, t, bins=8, method="quantile")
    assert all(n < 8 for n in b.n_bins)
    assert all(n >= 2 for n in b.n_bins)
    r = pid_williams_beer(b.joint)
    assert r.atoms() == pytest.approx(EXAMPLE_ATOMS["xor"], abs=ATOL)
    # Some bin counts leave only the edges {min, max}; the single closed
    # bin then contains every point.
    b1 = discretise_to_joint(s1, s2, t, bins=3, method="quantile")
    assert b1.n_bins == (1, 1, 1)
    assert b1.joint.shape == (1, 1, 1)
    assert b1.joint[0, 0, 0] == pytest.approx(1.0, abs=ATOL)


def test_rejects_bad_inputs() -> None:
    with pytest.raises(ValueError, match="3-D"):
        pid_williams_beer(np.ones((2, 2)))
    with pytest.raises(ValueError, match="negative"):
        pid_williams_beer(np.array([[[-1.0]]]))
    with pytest.raises(ValueError, match="same length"):
        discretise_to_joint([0.0, 1.0], [0.0], [0.0, 1.0])
    with pytest.raises(ValueError, match="method"):
        discretise_to_joint([0.0, 1.0], [0.0, 1.0], [0.0, 1.0], method="kmeans")
    with pytest.raises(ValueError, match="bins"):
        discretise_to_joint([0.0, 1.0], [0.0, 1.0], [0.0, 1.0], bins=0)


def test_self_checks_pass() -> None:
    lines = self_checks()
    assert len(lines) >= 5


if __name__ == "__main__":
    # Lightweight runner so the file can be executed without pytest's CLI.
    import traceback

    tests = [
        test_xor_synergy_one_others_zero,
        test_and_redundancy_and_synergy,
        test_copy_two_bit_documented_wb_values,
        test_rdn_redundancy_one,
        test_unq_unique1_one,
        test_dict_and_array_agree_on_xor,
        test_adapter_recovers_xor_from_discrete_points,
        test_adapter_binning_determinism,
        test_adapter_weights_equal_duplication,
        test_adapter_per_variable_bins_and_constant_column,
        test_quantile_merges_duplicate_edges,
        test_rejects_bad_inputs,
        test_self_checks_pass,
    ]
    for name in sorted(EXAMPLE_ATOMS):
        tests.append(lambda n=name: test_documented_gate_atoms(n))
    for shape in [(2, 2, 2), (3, 2, 4), (2, 5, 3), (4, 3, 5)]:
        tests.append(lambda s=shape: test_random_pmfs_nonnegative_and_atoms_sum(s))
    failed = 0
    for fn in tests:
        try:
            fn()
        except Exception as exc:  # pragma: no cover
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
            traceback.print_exc()
        else:
            print(f"ok   {fn.__name__}")
    if failed:
        raise SystemExit(1)
    print("OK: test_pid_williams_beer passed")
