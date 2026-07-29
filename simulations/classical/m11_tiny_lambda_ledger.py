#!/usr/bin/env python3
"""
M11 Phase 2 — tiny closed combinator (SKI) load ledger.

Ontology (matches synthesis/m11-idem-to-load.md):
  Microstate: closed SKI term (nested applications of S, K, I)
  Channel step: one normal-order redex contraction (leftmost-outermost)
  Output Y_k: structural class of the term after k steps (serialized shape),
              under a fixed finite ensemble of starting terms (uniform)
  H_c: exact Shannon of the pushforward over the ensemble (finite support)

Load proxies (weights β'=γ'=δ'=1; no continuum constants):
  L_E  — mean active redex count before the step (complexity / work);
         also report mean |AST|/|AST|_ref as an alternate energy proxy
  L_S  — |ΔH_c| across the step (output-entropy flux over the ensemble)
  L_B  — fraction of ensemble members that still have ≥1 redex after the
         step (open computational futures / distinguishability budget)

Ensemble: fixed hand-built closed terms (no RNG). Deterministic reduction.

Non-claims (do not assert from this script):
  - continuum L(ρ,g) equality, L ≡ G, Einstein/Newton from SKI
  - GfE / dual-toy residual H_c identity; Church–Turing ↔ gravity
  - Kolmogorov complexity equality; continuum load clock

Run:
  .venv/bin/python simulations/classical/m11_tiny_lambda_ledger.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

# Terms: atoms 'S'|'K'|'I' or App(fun, arg) as a 2-tuple
Atom = str
Term = Union[Atom, Tuple["Term", "Term"]]

REF_AST_SIZE = 8  # hand-chosen scale for AST ratio — not continuum


def shannon(probs: Iterable[float], base: float = 2.0) -> float:
    h = 0.0
    logb = math.log(base)
    for p in probs:
        if p > 0.0:
            h -= p * math.log(p) / logb
    return h


def app(f: Term, x: Term) -> Term:
    return (f, x)


def is_atom(t: Term) -> bool:
    return isinstance(t, str)


def ast_size(t: Term) -> int:
    if is_atom(t):
        return 1
    f, x = t  # type: ignore[misc]
    return 1 + ast_size(f) + ast_size(x)


def serialize(t: Term) -> str:
    """Canonical structural class string (observable Y)."""
    if is_atom(t):
        return str(t)
    f, x = t  # type: ignore[misc]
    return f"({serialize(f)} {serialize(x)})"


def match_redex(t: Term) -> Optional[Term]:
    """
    If t is a redex root, return its contractum; else None.

    Rules:
      (I x)           → x
      ((K x) y)       → x
      (((S x) y) z)   → ((x z) (y z))
    """
    if is_atom(t):
        return None
    f, x = t  # type: ignore[misc]
    # (I x) → x
    if f == "I":
        return x
    if is_atom(f):
        return None
    g, a = f  # type: ignore[misc]
    # ((K a) x) → a
    if g == "K":
        return a
    if is_atom(g):
        return None
    h, aa = g  # type: ignore[misc]
    # (((S aa) a) x) → ((aa x) (a x))
    if h == "S":
        return app(app(aa, x), app(a, x))
    return None


def count_redexes(t: Term) -> int:
    """Count all redex roots in the tree (active work proxy)."""
    n = 0

    def walk(u: Term) -> None:
        nonlocal n
        if match_redex(u) is not None:
            n += 1
        if is_atom(u):
            return
        f, x = u  # type: ignore[misc]
        walk(f)
        walk(x)

    walk(t)
    return n


def step_normal_order(t: Term) -> Tuple[Term, bool]:
    """Contract the leftmost-outermost redex once. Returns (new_term, reduced?)."""
    m = match_redex(t)
    if m is not None:
        return m, True
    if is_atom(t):
        return t, False
    f, x = t  # type: ignore[misc]
    f2, red = step_normal_order(f)
    if red:
        return app(f2, x), True
    x2, red = step_normal_order(x)
    if red:
        return app(f, x2), True
    return t, False


def build_ensemble() -> List[Term]:
    """
    Hand-built finite ensemble — exact H_c, no sampling noise.

    Mix of normal forms and multi-step reducible terms so H_c evolves.
    """
    I, K, S = "I", "K", "S"
    return [
        # normal forms (idle stockpile — low L when alone)
        I,
        K,
        S,
        app(K, I),  # (K I) not a redex without second arg
        app(S, K),
        # one-step redexes
        app(I, I),
        app(I, K),
        app(app(K, I), S),
        app(app(K, S), I),
        app(app(K, K), K),
        # multi-step / S redexes
        app(app(app(S, K), I), I),
        app(app(app(S, I), I), K),
        app(app(app(S, K), K), I),
        app(app(app(S, I), K), I),
        # nested I
        app(I, app(I, K)),
        app(app(I, K), I),
    ]


@dataclass
class LedgerRow:
    k: int
    description: str
    H_c: float
    L_E: float
    L_S: float
    L_B: float
    L_disc: float
    mean_redex: float
    mean_ast_ratio: float
    frac_open: float
    notes: str


def ensemble_stats(terms: Sequence[Term]) -> Dict[str, float]:
    n = len(terms)
    mass = 1.0 / n
    counts: Dict[str, float] = {}
    redex_sum = 0.0
    ast_sum = 0.0
    open_n = 0
    for t in terms:
        label = serialize(t)
        counts[label] = counts.get(label, 0.0) + mass
        r = count_redexes(t)
        redex_sum += r
        ast_sum += ast_size(t)
        if r > 0:
            open_n += 1
    return {
        "H_c": shannon(counts.values()),
        "mean_redex": redex_sum / n,
        "mean_ast_ratio": (ast_sum / n) / REF_AST_SIZE,
        "frac_open": open_n / n,
        "n_classes": float(len(counts)),
    }


def run_tiny_lambda_ledger(max_steps: int = 6) -> List[LedgerRow]:
    current = build_ensemble()
    n = len(current)
    rows: List[LedgerRow] = []

    st0 = ensemble_stats(current)
    rows.append(
        LedgerRow(
            k=0,
            description="ensemble at k=0 (before reduction)",
            H_c=st0["H_c"],
            L_E=0.0,
            L_S=0.0,
            L_B=0.0,
            L_disc=0.0,
            mean_redex=st0["mean_redex"],
            mean_ast_ratio=st0["mean_ast_ratio"],
            frac_open=st0["frac_open"],
            notes=(
                f"n={n} terms; classes={int(st0['n_classes'])}; "
                f"idle normals present — stockpile ≠ load"
            ),
        )
    )

    for k in range(1, max_steps + 1):
        mean_redex_pre = ensemble_stats(current)["mean_redex"]
        prev_H = rows[-1].H_c

        nxt: List[Term] = []
        for t in current:
            t2, _ = step_normal_order(t)
            nxt.append(t2)
        current = nxt

        st = ensemble_stats(current)
        H_c = st["H_c"]
        L_E = mean_redex_pre
        L_S = abs(H_c - prev_H)
        L_B = st["frac_open"]
        L_disc = L_E + L_S + L_B
        rows.append(
            LedgerRow(
                k=k,
                description=f"after {k} normal-order step(s)",
                H_c=H_c,
                L_E=L_E,
                L_S=L_S,
                L_B=L_B,
                L_disc=L_disc,
                mean_redex=st["mean_redex"],
                mean_ast_ratio=st["mean_ast_ratio"],
                frac_open=st["frac_open"],
                notes=(
                    f"classes={int(st['n_classes'])}; "
                    f"L_E=mean redexes pre-step; "
                    f"AST/ref={st['mean_ast_ratio']:.3f}"
                ),
            )
        )

    active = [r for r in rows if r.k > 0]
    assert active, "expected reduction steps"
    max_ls = max(r.L_S for r in active)
    assert max_ls > 0.0, "expected some ensemble entropy change under reduction"
    for r in active:
        assert abs(r.L_S - abs(r.H_c - rows[r.k - 1].H_c)) < 1e-12

    return rows


def format_table(rows: Sequence[LedgerRow]) -> str:
    header = (
        f"{'k':>3}  {'H_c':>8}  {'L_E':>6}  {'L_S':>8}  {'L_B':>8}  "
        f"{'L_disc':>8}  {'redex':>6}  {'AST/r':>6}  {'open':>6}  description"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.k:3d}  {r.H_c:8.5f}  {r.L_E:6.3f}  {r.L_S:8.5f}  {r.L_B:8.5f}  "
            f"{r.L_disc:8.5f}  {r.mean_redex:6.3f}  {r.mean_ast_ratio:6.3f}  "
            f"{r.frac_open:6.3f}  {r.description}"
        )
    return "\n".join(lines)


def _self_check_ski() -> None:
    I, K, S = "I", "K", "S"
    t, red = step_normal_order(app(I, K))
    assert red and t == K
    t, red = step_normal_order(app(app(K, I), S))
    assert red and t == I
    # S K I I → ((K I) (I I)) → I  (K-redex at root of second form)
    t0 = app(app(app(S, K), I), I)
    t1, red = step_normal_order(t0)
    assert red and serialize(t1) == "((K I) (I I))"
    t2, red = step_normal_order(t1)
    assert red and t2 == I
    # reduce a multi-step term to normal form
    cur = app(app(app(S, I), I), K)
    for _ in range(8):
        cur, red = step_normal_order(cur)
        if not red:
            break
    assert count_redexes(cur) == 0


def main() -> None:
    _self_check_ski()
    rows = run_tiny_lambda_ledger(max_steps=6)

    print("=" * 88)
    print("M11 Phase 2 — tiny SKI combinator load ledger")
    print("Design: synthesis/m11-idem-to-load.md §10 Phase 2 / ontology lambda")
    print("=" * 88)
    print()
    print(f"Ensemble size n = {len(build_ensemble())} fixed closed terms (uniform).")
    print("Observable Y_k = serialized term shape after k normal-order steps.")
    print(f"L_E primary = mean redex count pre-step; AST/ref uses ref={REF_AST_SIZE}.")
    print()
    print(format_table(rows))
    print()
    r0, r1 = rows[0], rows[1]
    print("Sanity:")
    print(f"  H_c(0)   = {r0.H_c:.6f} bits  (ensemble diversity at start)")
    print(f"  H_c(1)   = {r1.H_c:.6f} bits")
    print(f"  L_S(1)   = {r1.L_S:.6f}  (= |ΔH_c|)")
    print(f"  L_E(1)   = {r1.L_E:.6f}  (mean redexes before first step)")
    print(f"  L_disc max over k>0 = {max(r.L_disc for r in rows if r.k > 0):.6f}")
    last = rows[-1]
    print(f"  H_c({last.k})  = {last.H_c:.6f}; frac_open={last.frac_open:.3f}")
    print()
    print("Locked reading: L_S := |ΔH_c| so high flux ⇒ high L_S (PASS by construction).")
    print()
    print("NON-CLAIMS: not continuum L, not L≡G, not gravity, not dual-toy H_c;")
    print("            not Kolmogorov complexity; not continuum τ.")
    print("=" * 88)


if __name__ == "__main__":
    main()
