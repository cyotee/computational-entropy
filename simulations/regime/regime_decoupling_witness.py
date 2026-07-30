#!/usr/bin/env python3
"""
Stage 1 witness — does entropy production decouple from stress-energy?

Program: papers/REGIME_PROGRAM_dSc_decoupling.md (Stage 1, computational).

Question. The load term is  L = beta*E/(V*eps0) + gamma*|dS_c/dtau| + delta*bdy.
It departs from GR only if dS_c/dtau carries information NOT already in the
energy (stress-energy) term. This script tests, in an open-qubit model, whether
the entropy-production term is REABSORBABLE into the energy term, by realizing
the three regimes of the program:

  R1 — Pure dephasing (L = sqrt(rate)*sigma_z):
        coherences decay, populations fixed => energy E = Tr(rho H) CONSTANT,
        von Neumann S_c RISES. Candidate DECOUPLING (entropy at fixed energy,
        no heat flux into the system).
  R2 — Amplitude damping (L = sqrt(rate)*sigma_-):
        excited population relaxes => E CHANGES with S_c. Negative control;
        entropy rides with heat flux (in T_mu_nu) => reabsorbable.
  R3 — Two-qubit unitary (closed, entangling):
        global E conserved; a SUBSYSTEM's S_c rises. Definitional anchor:
        which coarse-graining defines S_c decides whether production exists.

Diagnostic. The coupling  kappa(t) = |dE/dt| / |dS_c/dt|  (energy per bit
produced). kappa = 0 <=> the entropy production is NOT accompanied by any
energy change => not reabsorbable into the energy term.

Clock. dtau/dt = 1 / (1 + alpha*L), compared for energy-only (GR-like) vs full
load. Weights alpha=beta=gamma=1 are STRUCTURAL bookkeeping (m11 convention),
NOT a physical calibration.

NON-CLAIMS: alpha,beta,gamma are uncalibrated; this shows the STRUCTURE of the
decoupling, not a physical magnitude. S_c is a model channel entropy, not the
gravitational load term; no gravity is asserted. Verdict feeds the regime
program, not a departure claim.

Run:
  .venv/bin/python simulations/regime/regime_decoupling_witness.py
"""

from __future__ import annotations

import numpy as np

# qubit basis: |0> ground (energy 0), |1> excited (energy omega)
OMEGA = 1.0
H1 = np.diag([0.0, OMEGA]).astype(complex)       # single-qubit Hamiltonian
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SM = np.array([[0, 1], [0, 0]], dtype=complex)   # sigma_-  = |0><1|  (lowering)
I2 = np.eye(2, dtype=complex)


def von_neumann_bits(rho: np.ndarray) -> float:
    """S(rho) in bits."""
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-15]
    return float(-np.sum(ev * np.log2(ev)))


def energy(rho: np.ndarray, H: np.ndarray) -> float:
    return float(np.real(np.trace(rho @ H)))


def lindblad_step(rho: np.ndarray, H: np.ndarray, Ls, dt: float) -> np.ndarray:
    """One explicit Euler step of the Lindblad master equation."""
    drho = -1j * (H @ rho - rho @ H)
    for L in Ls:
        Ld = L.conj().T
        drho += L @ rho @ Ld - 0.5 * (Ld @ L @ rho + rho @ Ld @ L)
    rho = rho + dt * drho
    # re-Hermitize / renormalize against Euler drift
    rho = 0.5 * (rho + rho.conj().T)
    rho = rho / np.real(np.trace(rho))
    return rho


def evolve_open(rho0, H, Ls, T=6.0, n=6000):
    dt = T / n
    ts, Es, Ss = [], [], []
    rho = rho0.copy()
    for k in range(n + 1):
        ts.append(k * dt)
        Es.append(energy(rho, H))
        Ss.append(von_neumann_bits(rho))
        if k < n:
            rho = lindblad_step(rho, H, Ls, dt)
    return np.array(ts), np.array(Es), np.array(Ss)


def rates(ts, Es, Ss):
    dE = np.gradient(Es, ts)
    dS = np.gradient(Ss, ts)
    return dE, dS


def clock_ratio(E, dS, alpha=1.0, beta=1.0, gamma=1.0):
    """dtau/dt for energy-only (GR-like) vs full load."""
    L_energy = beta * E
    L_full = beta * E + gamma * np.abs(dS)
    return 1.0 / (1.0 + alpha * L_energy), 1.0 / (1.0 + alpha * L_full)


def report_open(name, rho0, H, Ls):
    ts, Es, Ss = evolve_open(rho0, H, Ls)
    dE, dS = rates(ts, Es, Ss)
    # sample the peak in the INTERIOR (avoid np.gradient endpoint artifacts)
    m = len(ts)
    lo, hi = m // 50, m - m // 50
    i = lo + int(np.argmax(dS[lo:hi]))
    kappa = abs(dE[i]) / dS[i] if dS[i] > 1e-9 else float("nan")
    tau_e, tau_f = clock_ratio(Es, dS)
    print(f"\n--- {name} ---")
    print(f"  {'t':>5} {'E':>8} {'S(bits)':>8} {'dE/dt':>9} {'dS/dt':>8} "
          f"{'dtau/dt(E)':>11} {'dtau/dt(full)':>13}")
    for t in (0.5, 1.0, 2.0, 4.0):
        j = int(t / ts[-1] * (len(ts) - 1))
        print(f"  {ts[j]:5.2f} {Es[j]:8.4f} {Ss[j]:8.4f} {dE[j]:9.4f} "
              f"{dS[j]:8.4f} {tau_e[j]:11.5f} {tau_f[j]:13.5f}")
    print(f"  peak dS/dt at t={ts[i]:.2f}: |dE/dt|={abs(dE[i]):.2e}, dS/dt={dS[i]:.4f}"
          f"  =>  coupling kappa=|dE/dt|/|dS/dt| = {kappa:.2e}")
    return dict(name=name, maxAbsdE=float(np.max(np.abs(dE))), maxdS=float(np.max(dS)),
                kappa=kappa, dtau_gap=float(np.max(np.abs(tau_f - tau_e))))


def report_two_qubit_unitary():
    """R3: closed entangling unitary; global E fixed, subsystem S_c rises."""
    J = 1.0
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    H = J * np.kron(sx, sx)                      # entangling; [H,H]=0 => <H> conserved
    # |0>|0>: U(t)|00> = cos(Jt)|00> - i sin(Jt)|11>  (a Bell-type state; qubit 1
    # reduces to a mixture => subsystem S_c rises), while <H> = 0 is conserved.
    zero = np.array([1, 0], dtype=complex)
    psi0 = np.kron(zero, zero)
    ev, V = np.linalg.eigh(H)
    ts = np.linspace(0, 4.0, 400)
    Eg, S1 = [], []
    for t in ts:
        U = V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
        psi = U @ psi0
        Eg.append(float(np.real(psi.conj() @ (H @ psi))))
        # reduced density matrix of qubit 1
        psi_m = psi.reshape(2, 2)
        rho1 = psi_m @ psi_m.conj().T
        S1.append(von_neumann_bits(rho1))
    Eg, S1 = np.array(Eg), np.array(S1)
    print("\n--- R3: two-qubit entangling unitary (closed) ---")
    print(f"  global energy <H>: min={Eg.min():.2e}, max={Eg.max():.2e}  (conserved)")
    print(f"  subsystem S_c(qubit 1): min={S1.min():.4f}, max={S1.max():.4f} bits (rises)")
    print("  => coarse-graining DEFINES S_c: global production = 0, subsystem > 0.")
    return dict(name="R3", global_E_span=float(Eg.max() - Eg.min()), sub_S_max=float(S1.max()))


def main():
    print("=" * 76)
    print("Stage 1 — entropy-production vs stress-energy decoupling (open-qubit)")
    print("Design: papers/REGIME_PROGRAM_dSc_decoupling.md")
    print("=" * 76)

    plus = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex)  # |+><+|, E=0, S=0

    r1 = report_open("R1 pure dephasing (L=sqrt(g) sigma_z)", plus, H1,
                     [np.sqrt(0.8) * SZ])
    r2 = report_open("R2 amplitude damping (L=sqrt(g) sigma_-)", plus, H1,
                     [np.sqrt(0.8) * SM])
    r3 = report_two_qubit_unitary()

    # --- checks encoding the physics ---
    assert r1["maxAbsdE"] < 1e-6 and r1["maxdS"] > 0.5, \
        "R1 must produce entropy at (numerically) constant energy"
    assert r2["maxAbsdE"] > 1e-2 and r2["maxdS"] > 0.1, \
        "R2 must couple energy change to entropy production"
    assert r1["kappa"] < 1e-4 < r2["kappa"], \
        "coupling kappa must be ~0 for R1 (decoupled) and >0 for R2 (coupled)"
    assert r3["global_E_span"] < 1e-6 and r3["sub_S_max"] > 0.1, \
        "R3 must conserve global energy while a subsystem's S_c rises"

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    print(f"  R1 dephasing : dS/dt>0 at dE/dt=0  (kappa={r1['kappa']:.1e})  => DECOUPLED")
    print(f"  R2 damping   : dS/dt>0 with dE/dt<0 (kappa={r2['kappa']:.2f})  => COUPLED (heat in T_munu)")
    print(f"  R3 unitary   : global E fixed, subsystem S_c up  => coarse-graining defines S_c")
    print()
    print("  ==> The entropy-production term is NOT generally reabsorbable into the")
    print("      energy term: pure dephasing produces S_c at fixed local energy with")
    print("      no heat flux, so it lies outside the (local) stress-energy. The")
    print("      'always reformulation via reabsorption' horn is RULED OUT for R1;")
    print("      a departure exists IN PRINCIPLE. The full load clock dilates where")
    print(f"      the energy-only clock does not (R1 dtau gap {r1['dtau_gap']:.3f} at unit weights).")
    print()
    print("  CAVEAT (blocks Stage 3): alpha,beta,gamma are uncalibrated bookkeeping")
    print("  weights, so the physical MAGNITUDE is undetermined. Whether the effect")
    print("  is measurable (vs Planck-suppressed) needs a gamma calibration the")
    print("  framework has not fixed. Verdict: departure in principle; magnitude open.")
    print("\nNON-CLAIMS: no gravity asserted; S_c is a model channel entropy; unit")
    print("weights are structural, not physical. Feeds the regime program only.")
    print("=" * 76)


if __name__ == "__main__":
    main()
