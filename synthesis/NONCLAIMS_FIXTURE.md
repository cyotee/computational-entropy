# Non-claims fixture (mandatory list)

**Status:** Track A failure-mode fixture · 2026-07-15  
**Authority:** [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) §3 · [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2.3  
**Gate:** [CLAIM_GATE.md](CLAIM_GATE.md)  
**Checker:** [`simulations/classical/check_claim_hygiene.py`](../simulations/classical/check_claim_hygiene.py)

Do **not** expand this into proofs. Mirror only. Prefer under-claiming.

---

## 1. Frozen non-claims (CURRENT_CLAIMS §3)

Do **not** assert without new work:

| ID | Non-claim |
|----|-----------|
| N1 | Master equation \(\Leftrightarrow\) Bianconi continuum GfE. |
| N2 | \(L \equiv G\), \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\), \(\alpha_L\beta_L \equiv \alpha_B/\beta_B\). |
| N3 | T1 residual domination for all \(t\in(0,t_\star]\) (false; use T1′ / \(U_\star\)). |
| N4 | Pure T1′ with **no** soft hypotheses (PCRH\(_b\) still ensemble-certified). |
| N5 | Newton from pointwise \(\Phi\propto\rho\) Laplacian (**withdrawn**). |
| N6 | Next-order \(\gamma_L,\delta_L\) equal GfE \(D_{\mu\nu},\Lambda_G\). |
| N7 | Lattice denoising = empirical gravity. |
| N8 | External GfE papers established on par with GR. |
| N9 | IDEM/decay fully constructs continuum \(L\) or \(G\) (open / deferred). |

**Also (dual / M10 extras):** no theorem-level multi-jump / 2D / continuum SPDE residual domination; toy \(H_c\) \(\neq\) von Neumann \(S_c\) identity; M11 discrete accounting \(\neq\) continuum derivation; no Einstein from AND/SKI/shoe.

---

## 2. Forbidden phrase patterns (grep hints — not legal prose)

Lightweight patterns agents/scripts may flag when they appear as **positive** identities (negated / refused contexts are OK):

| Pattern (regex-ish) | Why |
|---------------------|-----|
| `L\s*≡\s*G` / `L \equiv G` / `L = G` as identity | Type safety |
| `master equation.*(equivalent|⇔|identical).*GfE` | N1 |
| `S_c\s*≡\s*Tr` / `S_c ≡ Tr g` | N2 |
| `α_L\s*β_L\s*=\s*α_B` / `alpha_L beta_L = alpha_B` | N2 constants |
| `Φ ∝ ρ` + Laplacian Newton / `Phi propto rho` recovery | N5 withdrawn |
| `lattice denoising` = `empirical gravity` | N7 |
| `IDEM.*(constructs\|derives).*(continuum L\|metric G)` | N9 |
| bare theory claim `H_c` without toy/disc/game tag when dual/M11/game mixed | M10 |

**Soft rule:** Do not fail a file solely because it *quotes* a non-claim to refuse it. Fail when the surrounding claim asserts the forbidden identity.

---

## 3. Banner language (expected in key docs)

These living docs should retain non-claims / type-safety language:

| File | Expected marker (substring) |
|------|-----------------------------|
| `synthesis/CURRENT_CLAIMS.md` | `Explicit non-claims` |
| `PROGRESS_REPORT.md` | `Explicit non-claims` |
| `papers/06-synthesis/OUTLINE.md` | `Non-claims banner` |
| `synthesis/CLAIM_GATE.md` | `Pass/fail` or `G1` |
| `GLOSSARY.md` | `L` and type safety / layers |

Checker prints presence of these markers; missing marker → warning (not hard fail unless `--strict`).

---

## 4. How to run the checker

```bash
.venv/bin/python simulations/classical/check_claim_hygiene.py
.venv/bin/python simulations/classical/check_claim_hygiene.py --strict
.venv/bin/python simulations/classical/check_claim_hygiene.py --grep
```

- Default: verify gate files exist; print frozen N1–N9; check banner markers.  
- `--grep`: scan a small allowlist of claim-bearing paths for forbidden **positive** phrases (lightweight; may false-positive on refusals — human review).  
- `--strict`: exit non-zero if required files or banner markers missing.

---

*Update only when CURRENT_CLAIMS §3 changes. Link; do not fork a second non-claims story.*
