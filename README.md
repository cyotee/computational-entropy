# Computational Entropy

**Preliminary research.** Supporting constructions and numerical ledgers are real; **nothing here has GR-level certainty.**

Research program on **computational entropy** (entropy of a map/channel’s **output** distribution), the gravitational channel \(\Phi_g\) with dimensionless **load** \(L\), and a staged bridge to continuum Gravity-from-Entropy (GfE) — without claiming master-equation \(\Leftrightarrow\) full continuum GfE or \(L \equiv G\).

## Live documentation site

**[https://cyotee.github.io/computational-entropy/](https://cyotee.github.io/computational-entropy/)**

Hosts the **full integrated paper** (`papers/06-synthesis/PAPER.md`) as navigable chapters (including §6 load equation), plus short canonical reference pages. Built with MkDocs from an allowlist — not a dump of drafts or agent notes.

Direct link to load / master equation on the site:  
[§6. Channel, load & master equation](https://cyotee.github.io/computational-entropy/papers/chapters/06-channel-load-master-equation/)

## Quick map (repository)

| Role | Path |
|------|------|
| **Integrated paper (source)** | [`papers/06-synthesis/PAPER.md`](papers/06-synthesis/PAPER.md) |
| Canonical \(H_c\) / \(S_c\) | [`foundations/computational-entropy/definition.md`](foundations/computational-entropy/definition.md) |
| \(\Phi_g\), load, master equation | [`emergent-gravity/master-equation.md`](emergent-gravity/master-equation.md) |
| Frozen claims / non-claims | [`synthesis/CURRENT_CLAIMS.md`](synthesis/CURRENT_CLAIMS.md) |
| Program conclusions | [`synthesis/PROGRAM_CONCLUSIONS.md`](synthesis/PROGRAM_CONCLUSIONS.md) |
| Final freeze report | [`papers/06-synthesis/FINAL.md`](papers/06-synthesis/FINAL.md) |
| Session bootstrap | [`PROGRESS_REPORT.md`](PROGRESS_REPORT.md) |
| Site plan | [`GITHUB_PAGES_PLAN.md`](GITHUB_PAGES_PLAN.md) |

**Type safety:** load \(L\) is a dimensionless **scalar**; structure metric \(G\) is a **metric**. \(L \neq G\).

## Local site preview

```bash
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/python scripts/sync_site_docs.py
.venv/bin/python -m mkdocs serve
```

Or: `bash scripts/build_site.sh` then open `site/index.html`.

## Premise (one paragraph)

Any map that transforms inputs induces an output distribution. **Computational entropy** measures that output entropy (Shannon / differential \(H_c\), or von Neumann \(S_c\) for channels), independent of internal algorithm. Two maps with the same output entropy are informationally equivalent for that measure. Gravity work in this repo models demand via load \(L\) and a master equation with load-gated proper time \(d\tau = dt/(1+\alpha L)\). See the [canonical definition](foundations/computational-entropy/definition.md) and [master equation](emergent-gravity/master-equation.md) rather than historical root drafts.

## Non-claims (summary)

Do not assert without new work: master equation \(\Leftrightarrow\) continuum GfE; \(L \equiv G\); residual dual for all \(t\); pointwise Laplacian Newton (withdrawn); lattice denoising as empirical gravity; IDEM fully constructing continuum \(L\) or \(G\). Full list on the site: [Non-claims](https://cyotee.github.io/computational-entropy/non-claims/).

## License

See [LICENSE.md](LICENSE.md).
