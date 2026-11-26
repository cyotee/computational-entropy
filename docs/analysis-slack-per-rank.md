# Slack of the corrected bound at readout ranks 2–16 (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model**.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim.

**Status:** 2026-11-26 · computed from existing output. No new simulation. The numbers are recomputed from the deterministic joint-law quantities already produced by the sixteen-symbol (two-use, rank-\(r\in\{2,4,8,16\}\)) surface runs:

- Haar-50 pool, [procedural-share-surface.md](procedural-share-surface.md) (CE-9; `procedural_share_surface.py`, seed 2026, SHA-256 `114e410f9fcf4700…`).
- ML-200 pool, [procedural-share-mlpool.md](procedural-share-mlpool.md) (CE-12; `procedural_share_mlpool.py`, canonical draw 2026, \(\varepsilon=0.05\), SHA-256 `d11fa3d1ec4594b7…`, 200 representatives).

Blind input (CE-9 half encoding). The GAD temperatures \(T\in\{0,1,\infty\}\) are the CE-9 settings; the CE-12 write-up reports \(T=1\) and dephasing, and the same existing `surface()` path is used here at \(T=0\) and \(T=\infty\) on the CE-12 pool (the pool does not depend on the channel). Dephasing on the Haar-50 pool is the CE-9 pool run through that same CE-12 path; it is not a table in the original CE-9 note. Nested Z is the primary readout; the random-basis control is summarized.

**Script:** [`simulations/classical/analysis_slack_per_rank.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/analysis_slack_per_rank.py). Pure numpy; calls the existing surface hooks only; no new sampling and no parameter change. Built-in self-checks lock the printed headlines below. Every number in the tables is printed by:

```
python simulations/classical/analysis_slack_per_rank.py
```

The slack is \(H(Y)-I(X;Y)-I(F;Y)\), i.e. the slack of the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\). With \(X\perp F\) (checked on the ML surfaces; a modelling fact of the blind encoding), this equals \(H(Y\mid X,F)+I(X;F\mid Y)\). No images are committed: the shape against \(g\) is the table.

## Result

The procedural share \(H(F\mid Y)\) does **not** collapse toward zero at rank 16, and the corrected-bound slack does **not** vanish there except in one case that is already present at every lower rank.

- At rank 16, \(g=0\), \(H(F\mid Y)\) is 5.338 bits on the Haar-50 pool (\(\log_2 50=5.644\)) and 7.339 bits on the ML-200 pool (\(\log_2 200=7.644\)). The drop from rank 2 to rank 16 is 0.271 bits (Haar) and 0.260 bits (ML). At \(g=1\) under GAD, \(H(F\mid Y)\) equals the pool entropy at every rank. The original form \(I(X;Y)+H(F\mid Y)\le H(Y)\) would have required \(H(F\mid Y)\le H(Y)-I(X;Y)\le 4\) bits at rank 16; that drop does not occur. The original form holds at 0 of 44 points (fails 44/44) on every surface below. The corrected bound holds at 44/44, as a theorem in this joint law.
- Slack at rank 16, GAD \(T=1\), nested Z: Haar-50 min / median / max over \(g\) is 3.360 / 3.741 / 3.818 bits (\(g=0\): 3.647; \(g=1\): 3.360). ML-200: 3.360 / 3.649 / 3.741 bits (\(g=0\): 3.552; \(g=1\): 3.360). Both are of the same order as \(H(Y)\) itself (\(I(X;Y)\) and \(I(F;Y)\) are at most 0.035 and 0.306 bits on Haar, 0.108 and 0.305 bits on ML). The shape against \(g\) at rank 16 matches the lower ranks, scaled by the larger output alphabet: a mid-grid hump at \(T=1\), a fall to 0 at \(g=1\) when \(T=0\), and a rise to \(\log_2 r\) at \(g=1\) when \(T=\infty\).
- The only place slack is 0 at rank 16 is GAD \(T=0\), \(g=1\) (plain amplitude damping), where the output is \(\lvert 0\rangle^{\otimes 4}\) and \(H(Y)=0\). That vanishing happens at **every** rank, not just 16. It is a full reset of the channel, not a resolution effect. The original form still fails there, because \(H(F\mid Y)=\log_2\lvert\mathrm{pool}\rvert>0=H(Y)\).
- \(H(Y)\le 4\) bits at rank 16, as it must: one block is two channel uses, and the 16-symbol alphabet has entropy at most 4 bits, against a pool entropy of 5.644 or 7.644 bits.

## Per-rank slack (bits)

Min / median / max are over the 11-point \(g\)-grid at that setting. Endpoints are \(g=0\) / \(g=1\).

| surface | r=2 min/med/max | r=2 g=0 / g=1 | r=4 min/med/max | r=4 g=0 / g=1 | r=8 min/med/max | r=8 g=0 / g=1 | r=16 min/med/max | r=16 g=0 / g=1 |
|---|---|---|---|---|---|---|---|---|
| Haar-50, GAD \(T=0\), nested | 0.000 / 0.804 / 0.966 | 0.965 / 0.000 | 0.000 / 1.586 / 1.867 | 1.840 / 0.000 | 0.000 / 2.389 / 2.825 | 2.792 / 0.000 | 0.000 / 3.169 / 3.715 | 3.647 / 0.000 |
| Haar-50, GAD \(T=1\), nested | 0.840 / 0.954 / 0.973 | 0.965 / 0.840 | 1.680 / 1.871 / 1.912 | 1.840 / 1.680 | 2.520 / 2.810 / 2.880 | 2.792 / 2.520 | 3.360 / 3.741 / 3.818 | 3.647 / 3.360 |
| Haar-50, GAD \(T=\infty\), nested | 0.965 / 0.991 / 1.000 | 0.965 / 1.000 | 1.840 / 1.975 / 2.000 | 1.840 / 2.000 | 2.792 / 2.965 / 3.000 | 2.792 / 3.000 | 3.647 / 3.948 / 4.000 | 3.647 / 4.000 |
| Haar-50, dephasing, nested | 0.965 / 0.965 / 0.965 | 0.965 / 0.965 | 1.840 / 1.840 / 1.840 | 1.840 / 1.840 | 2.792 / 2.792 / 2.792 | 2.792 / 2.792 | 3.647 / 3.647 / 3.647 | 3.647 / 3.647 |
| Haar-50, GAD \(T=1\), random | 0.991 / 0.998 / 1.000 | 0.991 / 1.000 | 1.951 / 1.979 / 1.985 | 1.973 / 1.951 | 2.928 / 2.983 / 2.987 | 2.928 / 2.984 | 3.866 / 3.959 / 3.970 | 3.866 / 3.959 |
| ML-200, GAD \(T=0\), nested | 0.000 / 0.794 / 0.937 | 0.929 / 0.000 | 0.000 / 1.521 / 1.811 | 1.792 / 0.000 | 0.000 / 2.313 / 2.741 | 2.711 / 0.000 | 0.000 / 3.039 / 3.602 | 3.552 / 0.000 |
| ML-200, GAD \(T=1\), nested | 0.840 / 0.934 / 0.953 | 0.929 / 0.840 | 1.680 / 1.834 / 1.872 | 1.792 / 1.680 | 2.520 / 2.770 / 2.822 | 2.711 / 2.520 | 3.360 / 3.649 / 3.741 | 3.552 / 3.360 |
| ML-200, GAD \(T=\infty\), nested | 0.929 / 0.983 / 1.000 | 0.929 / 1.000 | 1.792 / 1.963 / 2.000 | 1.792 / 2.000 | 2.711 / 2.945 / 3.000 | 2.711 / 3.000 | 3.552 / 3.925 / 4.000 | 3.552 / 4.000 |
| ML-200, dephasing, nested | 0.929 / 0.929 / 0.929 | 0.929 / 0.929 | 1.792 / 1.792 / 1.792 | 1.792 / 1.792 | 2.711 / 2.711 / 2.711 | 2.711 / 2.711 | 3.552 / 3.552 / 3.552 | 3.552 / 3.552 |
| ML-200, GAD \(T=1\), random | 0.989 / 0.998 / 1.000 | 0.989 / 1.000 | 1.951 / 1.978 / 1.984 | 1.974 / 1.951 | 2.919 / 2.980 / 2.986 | 2.919 / 2.984 | 3.857 / 3.958 / 3.967 | 3.857 / 3.959 |

At \(g=1\) under GAD the two pools agree (the output state no longer depends on the candidate or the message). Nested dephasing is flat in \(g\) and equals the \(g=0\) GAD row, because pure dephasing is invisible to a Z readout, as in CE-12. The random-basis control is not a coarse-graining across ranks; its rank-16 slack is also large (median 3.959 Haar, 3.958 ML at \(T=1\)) and does not vanish.

## Slack versus \(g\), nested Z (bits)

**Haar-50, GAD \(T=1\), nested**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.965 | 1.840 | 2.792 | 3.647 |
| 0.1 | 0.971 | 1.881 | 2.843 | 3.741 |
| 0.2 | 0.973 | 1.904 | 2.871 | 3.795 |
| 0.3 | 0.971 | 1.912 | 2.880 | 3.818 |
| 0.4 | 0.964 | 1.909 | 2.872 | 3.815 |
| 0.5 | 0.954 | 1.895 | 2.848 | 3.788 |
| 0.6 | 0.940 | 1.871 | 2.810 | 3.741 |
| 0.7 | 0.921 | 1.837 | 2.758 | 3.674 |
| 0.8 | 0.899 | 1.794 | 2.693 | 3.588 |
| 0.9 | 0.872 | 1.742 | 2.613 | 3.483 |
| 1.0 | 0.840 | 1.680 | 2.520 | 3.360 |

**ML-200, GAD \(T=1\), nested**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.929 | 1.792 | 2.711 | 3.552 |
| 0.1 | 0.942 | 1.834 | 2.770 | 3.649 |
| 0.2 | 0.950 | 1.860 | 2.805 | 3.708 |
| 0.3 | 0.953 | 1.872 | 2.822 | 3.737 |
| 0.4 | 0.952 | 1.872 | 2.822 | 3.741 |
| 0.5 | 0.945 | 1.862 | 2.807 | 3.723 |
| 0.6 | 0.934 | 1.843 | 2.777 | 3.685 |
| 0.7 | 0.918 | 1.815 | 2.733 | 3.630 |
| 0.8 | 0.897 | 1.778 | 2.676 | 3.557 |
| 0.9 | 0.871 | 1.733 | 2.605 | 3.467 |
| 1.0 | 0.840 | 1.680 | 2.520 | 3.360 |

**Haar-50, GAD \(T=0\), nested** (plain amplitude damping; \(g=1\) resets the output)

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.965 | 1.840 | 2.792 | 3.647 |
| 0.1 | 0.966 | 1.867 | 2.825 | 3.715 |
| 0.2 | 0.951 | 1.853 | 2.798 | 3.694 |
| 0.3 | 0.919 | 1.801 | 2.717 | 3.595 |
| 0.4 | 0.871 | 1.712 | 2.581 | 3.420 |
| 0.5 | 0.804 | 1.586 | 2.389 | 3.169 |
| 0.6 | 0.718 | 1.418 | 2.135 | 2.834 |
| 0.7 | 0.608 | 1.202 | 1.810 | 2.403 |
| 0.8 | 0.469 | 0.927 | 1.396 | 1.854 |
| 0.9 | 0.287 | 0.568 | 0.855 | 1.136 |
| 1.0 | 0.000 | 0.000 | 0.000 | 0.000 |

**ML-200, GAD \(T=0\), nested:** the same fall-to-zero shape, slightly smaller values (rank 16: 3.552 at \(g=0\), median 3.039, 0 at \(g=1\)). **At \(T=\infty\), nested,** slack rises with \(g\) to \(\log_2 r\) at \(g=1\) (Haar rank 16: 3.647 → 4.000, median 3.948; ML rank 16: 3.552 → 4.000, median 3.925). The \(g=0\) row is independent of \(T\).

## \(H(F\mid Y)\) at the endpoints (bits)

| surface | \(H(F\mid Y)\) at \(g=0\), r=2/4/8/16 | \(H(F\mid Y)\) at \(g=1\), r=2/4/8/16 |
|---|---|---|
| Haar-50, GAD \(T=1\), nested (all \(T\) agree at \(g=0\)) | 5.609 / 5.486 / 5.453 / 5.338 | 5.644 / 5.644 / 5.644 / 5.644 |
| ML-200, GAD \(T=1\), nested (all \(T\) agree at \(g=0\)) | 7.599 / 7.487 / 7.444 / 7.339 | 7.644 / 7.644 / 7.644 / 7.644 |
| Haar-50, dephasing, nested (flat in \(g\)) | 5.609 / 5.486 / 5.453 / 5.338 | 5.609 / 5.486 / 5.453 / 5.338 |
| ML-200, dephasing, nested (flat in \(g\)) | 7.599 / 7.487 / 7.444 / 7.339 | 7.599 / 7.487 / 7.444 / 7.339 |

The Haar \(T=1\) nested row is the published CE-9 table. Under GAD at \(g=1\), \(H(F\mid Y)=\log_2\lvert\mathrm{pool}\rvert\) at every rank because the output is independent of the candidate.

## Caveats

The nested readouts are exact coarse-grainings: rank \(r\) is a deterministic function of rank \(2r\). By data processing, the trends of \(H(Y)\), \(I(X;Y)\) and \(I(F;Y)\) with rank are constrained by construction, and so is the slack. A slack that stays of order \(H(Y)\) at rank 16 shows that, in this toy channel, the corrected bound's slack is not an artifact of coarse measurement. It does **not** show that the inequality is fundamental.

\(H(Y)\le 4\) bits at rank 16 is likewise by construction (two-use blocks, a 16-symbol alphabet). The pool entropies 5.644 and 7.644 bits sit above that cap, which is why the original form cannot hold at any rank once \(H(F\mid Y)\) stays near the pool entropy.

## Scope

Tier 2 only. A two-qubit, two-use toy with a fixed candidate pool, a fixed encoding, and the readouts and channels already used in CE-9 and CE-12. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this readout beyond the bookkeeping above.
