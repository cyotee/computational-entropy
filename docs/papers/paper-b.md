# An Information-Theoretic Reformulation of Thermodynamic Gravity (Conjecture)

**Paper B (conjecture) — Draft**
**Status:** 2026-07-29 · Preliminary research · position / research-programme paper
**Scope contract:** [../DELIVERY_SCOPE.md](../DELIVERY_SCOPE.md) §2 (may assert B1–B7; non-claims N1–N9)
**Depends on:** Paper A [../01-foundations/PAPER_A_computational_entropy.md](../01-foundations/PAPER_A_computational_entropy.md)
**Falsifiability verdict:** [../FALSIFIABILITY_L_vs_GR.md](../FALSIFIABILITY_L_vs_GR.md)
**Canonical dynamics:** [../../emergent-gravity/master-equation.md](../../emergent-gravity/master-equation.md) · **Newton:** [../../emergent-gravity/recoveries/newtonian/README.md](../../emergent-gravity/recoveries/newtonian/README.md)

---

## Abstract

Building on the computational-entropy framework of Paper A — where the entropy of a channel's **output** distribution is a well-defined, Landauer-exact quantity — we ask whether gravity's known thermodynamic character can be *re-expressed* in this vocabulary. We define a gravitational channel \(\Phi_g\) and a scalar **computational load** \(L\) that reparameterizes proper time, and we present the resulting master equation **honestly as a postulate with a Jacobson-consistent shape**, not as a derivation. Under this postulate the Newtonian weak field is recovered only along an imported route (Clausius → Einstein → Poisson) with one on-shell calibration; we do not derive Newton or Newton's constant from information alone. We report that our framework and continuum Gravity-from-Entropy reach the same leading Poisson equation (a *weak* agreement forced by both embedding Einstein at low coupling) while diverging at next order. Our central result is therefore **negative-leaning and clarifying**: as constructed the framework is an **information-theoretic reformulation** of thermodynamic gravity, making no sharp prediction distinct from general relativity in any currently accessible regime. We isolate the single term of \(L\) — the computational-entropy-production term — where a genuine departure could live, state precisely the missing theorem that would turn it into a prediction, and flag either outcome (reformulation confirmed, or departure found) as acceptable.

---

## 1. Position (B1)

This paper is **not** a claim of a new theory of gravity. It is a claim that the *thermodynamic/entropic* content already present in Jacobson's and Verlinde's programs can be repackaged in the computational-entropy language of Paper A, and an honest map of exactly how far that repackaging currently reaches. Whether it ever becomes a genuine theory (a falsifiable departure from GR) is **open**; the falsifiability analysis (§6) records the current verdict as *reformulation*.

Every mapping below is tagged **semantic / structural / constructive**. Type safety is enforced throughout: the load \(L\) is a dimensionless scalar; a structure-induced metric \(G\) is a tensor; \(L\neq G\).

## 2. The gravitational channel and load (B2)

We model local microstate evolution as a CPTP **gravitational channel** \(\Phi_g\),


$$
\rho(\tau+\delta\tau)=\Phi_g[\rho(\tau);g_{\mu\nu}(\rho)], \qquad
S_c(\Phi_g;\rho)=S(\Phi_g(\rho)),
$$


with \(S_c\) the von Neumann output entropy (the quantum instance of Paper A's \(H_c\)). The instantaneous processing demand is the **computational load**


$$
L(\rho,g)=\beta\frac{E[\rho]}{V\epsilon_0}
+\gamma\left|\frac{dS_c}{d\tau}\right|_{\rm reg}
+\delta\frac{S_{\rm boundary}(\rho)}{S_{\rm BH}(A)},
$$


which clocks proper time via \(d\tau=dt/(1+\alpha L)\), giving the master equation


$$
\frac{d\rho}{dt}=\frac{1}{1+\alpha L(\rho,g)}\,\mathcal{L}_g[\rho;g_{\mu\nu}(\rho)].
$$


**Honesty statement (structural).** The generator \(\mathcal{L}_g\) is *required* to satisfy Clausius \(\delta Q=T\,dS_c\) on local horizons. This is exactly Jacobson's (1995) condition, from which the Einstein equations follow. The master equation is thus **postulated with the shape that makes it Jacobson-consistent** — it is not independently derived, and on-shell its geometry is GR by construction. What the framework adds beyond GR, if anything, lives entirely in the *clock* \(L\) (see §6).

## 3. Newton via Path J/M only (B3)

We recover the Newtonian weak field along one route, with rigor labels (canonical: [../../emergent-gravity/recoveries/newtonian/README.md](../../emergent-gravity/recoveries/newtonian/README.md)):

| Step | Content | Rigor |
|------|---------|-------|
| J | Clausius on \(\mathcal{L}_g\) ⇒ Einstein equations | **imported theorem** (Jacobson) + modeling assumption |
| — | Einstein weak field ⇒ \(\nabla^2\Phi=4\pi G\rho_m\) | standard GR |
| M | Load clock \(d\tau=dt/(1+\alpha L)\) matches Newtonian redshift **on shell**; \(\alpha\beta=4\pi G/c^4\) | **calibration** |

**Explicitly not claimed (N5):** the withdrawn pointwise identification \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\). **Not claimed:** a free first-principles value of \(G\), or Newton independent of the Jacobson/Einstein import.

## 4. Contact with continuum Gravity-from-Entropy (B4)

Comparing our framework to Bianconi's continuum GfE at low coupling (canonical: [../../synthesis/m6-weak-field-plugtest.md](../../synthesis/m6-weak-field-plugtest.md)):

| Criterion | Outcome |
|-----------|---------|
| Same leading Poisson \(\nabla^2\Phi=4\pi G\rho_m\) | **WEAK PASS** — both via Einstein/GR |
| Same derivation mechanism | **FAIL** |
| Identifiable \((\alpha_L,\beta_L)=(\alpha_B,\beta_B)\) | **FAIL / refused** |
| Next-order corrections match | **structural FAIL** — GfE extras live in the metric EOM (\(D_{\mu\nu},\Lambda_G\)); our \(\gamma_L,\delta_L\) live in the load clock unless *promoted* |

The Poisson agreement is **circumstantial co-class with GR**, not evidence that load dynamics equal Bianconi's relative-entropy equations of motion (non-claim N1).

## 5. The ACD-EW construction as analogy only (B5)

An earlier warm-up ("Action–Channel Duality, Euclidean") compares edge-preserving (Perona–Malik) diffusion to isotropic heat on a noisy 1D/2D signal, and finds the edge-preserving reconstructor wins residual on an intermediate time window. We include it **only as an analogy** to Bianconi's warm-up gradient flow. We note plainly that Perona–Malik edge-preserving diffusion is standard prior art from image processing, that the "field" there is a test signal on a flat lattice (not spacetime), and that the gravity payoff is **analogical, not evidential** (non-claim N7: lattice denoising ≠ empirical gravity). This thread is treated as **closed**, not an open crisis.

## 6. Falsifiability — the central open question (B6)

Since the geometry is GR on-shell, any departure must come from \(L\) depending on data not carried by the stress-energy \(T_{\mu\nu}\). Term by term (full analysis: [../FALSIFIABILITY_L_vs_GR.md](../FALSIFIABILITY_L_vs_GR.md)):

1. **Energy term** \(\beta E/V\epsilon_0\): a function of \(T_{\mu\nu}\), calibrated to GR redshift — **no new prediction**.
2. **Entropy-production term** \(\gamma|dS_c/d\tau|\): depends on the *rate of irreversible information processing*, which GR's proper time does **not** see — **the one candidate departure**.
3. **Boundary term** \(\delta S_{\rm boundary}/S_{\rm BH}\): only significant near horizons — quantum-gravity regime, not currently testable.

> **Verdict (recorded): REFORMULATION**, with the entropy-production term flagged as the single place a genuine GR departure could live. It is not yet a prediction because (a) degeneracy with an effective stress-energy contribution has not been excluded, and (b) the calibrated magnitude of \(\gamma\) is unknown.

**Central conjecture / missing theorem.** *Either* exhibit a regime in which \(dS_c/d\tau\) is **not** a function of \(T_{\mu\nu}\), compute the calibrated \(\gamma\)-residual, and derive a clock-rate prediction distinct from GR (→ a real experiment: precision timing across strongly irreversible / decoherence-heavy processes at fixed energy density); *or* prove a **degeneracy no-go** showing the three-term load is always reabsorbable into GR + effective source without promotion into the field equations. Either result closes the question and is acceptable.

## 7. O1 seed — one-slot continuum limit (B7, optional)

The discrete load slots of Paper A (\(L_S=H(X\mid Y)\), extensive; \(L_E\), extensive; \(L_B\), non-additive) are finite classical objects. A first constructive step toward a continuum \(L\) is to take **one slot only** — export \(L_S\) — on a lattice of local maps with extensive export, and ask whether a scaling limit yields a local export *density*. We present this as an **open first step**, not a completed construction (non-claim N9: IDEM/decay does not yet construct continuum \(L\) or \(G\)). The target statement: *"there is a scaling limit under which discrete export density converges to a continuum entropy-production density, with stated topology and rate — or a precise obstruction."*

## 8. Non-claims (frozen)

N1 master eq ⇎ continuum GfE · N2 \(L\not\equiv G\), \(S_c\not\equiv\operatorname{Tr}g\ln G^{-1}\) · N5 no pointwise-\(\rho\) Newton · N6 \(\gamma_L,\delta_L\neq D_{\mu\nu},\Lambda_G\) · N7 lattice ≠ gravity · N8 GfE not on par with GR · N9 no continuum \(L\)/\(G\) from IDEM · no free \(G\)-from-bits. Full list: [../../synthesis/CURRENT_CLAIMS.md](../../synthesis/CURRENT_CLAIMS.md) §3.

---

## Changelog

| Date | Entry |
|------|-------|
| 2026-07-29 | Initial draft: reformulation stance; channel/load postulate; Path J/M; M6 WEAK PASS/FAIL; ACD-EW as analogy; falsifiability verdict + central conjecture; O1 seed. |
