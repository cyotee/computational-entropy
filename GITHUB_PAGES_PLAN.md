# GitHub Pages Publishing Plan

**Status:** Plan only (2026-07-17) — not yet implemented  
**Repo:** `cyotee/computational-entropy`  
**Expected site URL:** `https://cyotee.github.io/computational-entropy/`  
**Related:** [PLAN.md](PLAN.md) (research reorg), [papers/06-synthesis/PUBLISHING.md](papers/06-synthesis/PUBLISHING.md) (standalone paper notes)

---

## 1. Goal

Publish a **public research site** for this program: definitions, master equation, frozen claims/non-claims, synthesis conclusions, and the human-facing papers — without dumping the entire working tree (agent bootstrap, drafts, build artifacts, copyright-sensitive PDFs) onto the open web as an unfiltered file dump.

**Success looks like:**

1. A navigable site with MathJax (or KaTeX) rendering of \(H_c\), \(S_c\), \(\Phi_g\), \(L\), etc.
2. A clear entry path for human readers (not agent bootstrap order).
3. Canonical research files remain single sources of truth; the site is a **presentation layer**, not a second copy of the theory.
4. CI builds and deploys on push to `master`.
5. Explicit non-claims and preliminary-research stance remain visible on landing and key pages.

---

## 2. What GitHub Pages requires

Official model (GitHub Docs):

| Item | Requirement |
|------|-------------|
| **Hosting** | Free for **public** repositories on GitHub Free |
| **Visibility** | Pages sites are **public on the internet** even if the repo is private (plan-dependent) — treat published content as public |
| **Entry file** | Built site must have `index.html` (or source `index.md` / `README.md` depending on method) at the artifact root |
| **Publishing source** | Either (A) **branch + folder** (`/` or `/docs` on a branch), or (B) **GitHub Actions** workflow that uploads a static artifact |
| **Static only** | No server-side Python/Ruby/PHP at runtime |
| **Jekyll default** | Branch-based deploys run Jekyll unless `.nojekyll` is present; custom SSGs should use Actions (recommended) |
| **Project site URL** | `https://<user>.github.io/<repo>/` → `https://cyotee.github.io/computational-entropy/` |
| **Custom domain** | Optional later via repo Settings → Pages |

### 2.1 Publishing-source options (choose one)

| Option | How it works | Fit for this repo |
|--------|----------------|-------------------|
| **A. Branch `/docs`** | Put site files in `docs/`; Settings → Pages → Deploy from branch → `/docs` | Simple, but native Jekyll math/nav is weak for this corpus |
| **B. `gh-pages` branch** | Build elsewhere; commit static HTML to `gh-pages` | Works with `mkdocs gh-deploy`; branch is generated noise |
| **C. GitHub Actions + Pages artifact (recommended)** | Workflow builds static site → `upload-pages-artifact` → `deploy-pages`; Settings → Pages → **Source: GitHub Actions** | Best control, no need to hand-maintain HTML; modern default |
| **D. Actions that force-push `gh-pages`** | Material for MkDocs classic `mkdocs gh-deploy` | Also fine; slightly older pattern |

**Recommendation:** **C** (official Pages Actions) or Material’s **D** if we prefer their documented one-liner. Prefer **C** for explicit permissions and PR build-without-deploy.

### 2.2 What we must *not* rely on

- Serving the **repo root as-is** as the site (root is agent + research workspace, not a site).
- Assuming GitHub’s Markdown viewer equals a site (no nav, weak multi-page UX).
- Publishing **all** Markdown without a allowlist (drafts, historical root `.markdown`, LaTeX aux files, agent docs).

---

## 3. Recommended stack

### 3.1 Primary recommendation: **MkDocs + Material for MkDocs**

| Why | Detail |
|-----|--------|
| Already Python | Repo has `.venv` and simulation tooling; add `mkdocs-material` to docs deps |
| Math | `pymdownx.arithmatex` + MathJax/KaTeX (critical for this theory) |
| Navigation | Explicit `nav:` for a research reading order |
| Search | Built-in client search |
| Deploy | Well-documented GitHub Actions path |
| Tone | Documentation/research sites (not blog-first) |

**Alternatives considered (not default):**

| Tool | Pros | Cons for this repo |
|------|------|--------------------|
| **Jekyll + Just the Docs** | Native Pages | Ruby toolchain; weaker for large scientific nav; not our Python ecosystem |
| **Quarto** | Excellent academic HTML/PDF | Heavier; better if primary goal is paper HTML only |
| **Docsify / raw Markdown** | Zero build | Weak offline/search; math plugins ad hoc |
| **Docusaurus** | Nice React site | Overkill; Node stack parallel to Python research |

### 3.2 Math delimiter policy (align with existing paper work)

From [papers/06-synthesis/PUBLISHING.md](papers/06-synthesis/PUBLISHING.md):

- Prefer **`$...$` / `$$...$$`** for portable rendering.
- Site pages that still use `\(...\)` / `\[...\]` should either be converted or configured so MathJax accepts both.
- Nested math modes are fragile — fix at source when a page is promoted to the site.

---

## 4. Content architecture: **site overlay, not full repo mirror**

Do **not** mass-move research trees into `docs/` in a way that breaks agent bootstrap (`PROGRESS_REPORT.md`, `foundations/`, `emergent-gravity/`, `synthesis/`). Policy remains **canonicalize-first** ([PLAN.md](PLAN.md), Claude.md).

### 4.1 Mental model

```text
┌─────────────────────────────────────────────────────────┐
│  Research workspace (source of truth)                   │
│  foundations/ · emergent-gravity/ · synthesis/ · papers/│
│  simulations/ · PROGRESS_REPORT.md · …                  │
└───────────────────────────┬─────────────────────────────┘
                            │  copy / symlink / include
                            │  (build step or thin wrappers)
                            ▼
┌─────────────────────────────────────────────────────────┐
│  docs/   ← MkDocs docs_dir (presentation tree)          │
│  index.md, nav structure, curated pages + assets        │
└───────────────────────────┬─────────────────────────────┘
                            │  mkdocs build
                            ▼
┌─────────────────────────────────────────────────────────┐
│  site/   ← static HTML (gitignored) → GitHub Pages      │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Two valid implementation styles

**Style S1 — Curated copies via build script (recommended first cut)**

- Maintain `docs/` with human-written landing pages + a small Python script `scripts/sync_site_docs.py` that **copies** allowlisted canonical Markdown into `docs/_content/...` before `mkdocs build`.
- Pros: explicit allowlist; easy to exclude agent/draft material; CI is deterministic.
- Cons: slight duplication at build time (not committed if script runs only in CI / pre-build).

**Style S2 — Thin wrapper pages that include or link**

- `docs/` pages are short front-matter stubs linking to GitHub blob URLs *or* using `pymdownx.snippets` / includes from outside `docs_dir`.
- Pros: less copy machinery.
- Cons: outside-`docs_dir` includes need careful config; GitHub-only links make a worse offline site.

**Default plan: S1** (allowlist + pre-build sync). Keep wrappers only for pages that must differ for web (landing, “how to read,” non-claims banner).

### 4.3 Proposed `docs/` tree (target)

```text
docs/
├── index.md                          # Public landing (rewrite of README for humans)
├── how-to-read.md                    # Reading order for visitors
├── non-claims.md                     # Explicit non-claims + type safety
├── glossary.md                       # from GLOSSARY.md
├── progress.md                       # from PROGRESS_REPORT.md (or trimmed public version)
├── foundations/
│   └── computational-entropy.md      # ← foundations/computational-entropy/definition.md
├── emergent-gravity/
│   ├── master-equation.md            # ← emergent-gravity/master-equation.md
│   └── newtonian-recovery.md         # ← recoveries/newtonian/README.md
├── synthesis/
│   ├── claims.md                     # ← CURRENT_CLAIMS.md
│   ├── conclusions.md                # ← PROGRAM_CONCLUSIONS.md
│   ├── open-avenues.md               # ← OPEN_AVENUES.md
│   ├── pack-index.md                 # ← PACK_INDEX.md (optional)
│   └── bridge-gfe.md                 # ← bridge-bianconi-relative-entropy.md (optional)
├── papers/
│   ├── final-report.md               # ← papers/06-synthesis/FINAL.md
│   ├── publishable.md                # ← PUBLISHABLE.md (standalone narrative)
│   └── integrated-paper.md           # ← PAPER.md (if math/links clean enough)
├── simulations/
│   ├── overview.md                   # ← simulations/README.md + honesty limits
│   └── figures/                      # selected PNGs from simulations/bridging/
└── assets/
    └── (logo, favicon, extra CSS if any)
```

Nav should emphasize: **landing → non-claims → foundations → master equation → claims → final report → open avenues**.

### 4.4 Publish allowlist (include)

| Priority | Source path | Site role |
|----------|-------------|-----------|
| P0 | New `docs/index.md` | Landing |
| P0 | `foundations/computational-entropy/definition.md` | Canonical \(H_c\)/\(S_c\) |
| P0 | `emergent-gravity/master-equation.md` | \(\Phi_g\), \(L\), master eq |
| P0 | `synthesis/CURRENT_CLAIMS.md` | Frozen claims |
| P0 | `synthesis/PROGRAM_CONCLUSIONS.md` | P1–P11 |
| P0 | `papers/06-synthesis/FINAL.md` and/or `PUBLISHABLE.md` | Program report |
| P1 | `GLOSSARY.md` | Notation |
| P1 | `PROGRESS_REPORT.md` | Status (consider a **public-trimmed** variant if agent-heavy) |
| P1 | `synthesis/OPEN_AVENUES.md` | Next research |
| P1 | `THEORY.md` | Bridge architecture (maybe abridged) |
| P1 | `emergent-gravity/recoveries/newtonian/README.md` | Newton Path J/M |
| P1 | Selected `simulations/bridging/*.png` + DESIGN honesty limits | Pattern witnesses only |
| P2 | `synthesis/action-channel-duality-euclidean.md` | ACD-EW |
| P2 | `synthesis/m11-idem-to-load.md` | IDEM → load design |
| P2 | Key M-series notes linked from PACK_INDEX | Deep dives |

### 4.5 Publish denylist (exclude by default)

| Path / pattern | Reason |
|----------------|--------|
| `CLAUDE.md`, agent-only bootstrap | Not for public readers |
| `PRD.md` (product/agent rules) | Internal process unless rewritten |
| `drafts/`, `archive/` | Historical / superseded |
| Root historical `*.markdown` | Uncurated legacy |
| `papers/external/*.pdf` | **Copyright / redistribution** — link arXiv IDs, do not rehost PDFs without license check |
| `external-docs/*.pdf` | Same |
| `*.aux`, `*.log`, `*.fls`, `*.fdb_latexmk`, `*.xdv`, `*.toc` | Build junk |
| `__pycache__/`, `.venv/`, notebooks checkpoints | Runtime noise |
| Full simulation Python (optional later) | Site can link to GitHub tree instead of hosting code |
| `quantum/*.tex` build intermediates | Prefer linked PDF or markdown twin if published |

### 4.6 Legal / honesty gates before go-live

1. **External PDFs:** Prefer arXiv abstract links in prose; do not ship peer PDFs on Pages unless license allows.
2. **Non-claims banner** on landing + final report (program stance: preliminary; no GR-level certainty).
3. **Joint toys / blackjack:** Label as **pattern witnesses**, not gravity confirmation or strategy ROI (existing honesty rules).
4. **Repo visibility:** Confirm `computational-entropy` is public (required for free Pages).

---

## 5. Repo restructuring (minimal invasive)

Goal: support the site **without** a second research reorg like full [PLAN.md](PLAN.md) canonicalize pass.

### 5.1 New top-level files / dirs

```text
computational-entropy/
├── mkdocs.yml                 # Site config (nav, theme, math, site_url)
├── docs/                      # Presentation tree (see §4.3)
├── requirements-docs.txt      # mkdocs-material + plugins (or docs group in pyproject)
├── scripts/
│   └── sync_site_docs.py      # Allowlist copy into docs/_content/
├── .github/workflows/
│   └── pages.yml              # Build + deploy Pages
├── GITHUB_PAGES_PLAN.md       # This plan
└── site/                      # mkdocs build output — gitignored
```

### 5.2 Config sketch (`mkdocs.yml`)

Essential settings to plan for:

```yaml
site_name: Computational Entropy
site_description: Computational entropy, load, and emergent-gravity research (preliminary)
site_url: https://cyotee.github.io/computational-entropy/
repo_url: https://github.com/cyotee/computational-entropy
repo_name: cyotee/computational-entropy
edit_uri: edit/master/docs/   # or disable if pages are generated copies

theme:
  name: material
  features:
    - navigation.sections
    - navigation.expand
    - search.suggest
    - content.code.copy
  palette:
    - scheme: default
      primary: indigo
      toggle:
        icon: material/brightness-7
    - scheme: slate
      primary: indigo
      toggle:
        icon: material/brightness-4

markdown_extensions:
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.superfences
  - pymdownx.details
  - admonition
  - toc:
      permalink: true
  - footnotes
  - tables

extra_javascript:
  - javascripts/mathjax.js   # small loader
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

plugins:
  - search
  # optional later: awesome-pages, git-revision-date-localized

nav:
  - Home: index.md
  - How to read: how-to-read.md
  - Non-claims: non-claims.md
  - Foundations:
      - Computational entropy: foundations/computational-entropy.md
  - Emergent gravity:
      - Master equation: emergent-gravity/master-equation.md
      - Newtonian recovery: emergent-gravity/newtonian-recovery.md
  - Synthesis:
      - Claims: synthesis/claims.md
      - Conclusions: synthesis/conclusions.md
      - Open avenues: synthesis/open-avenues.md
  - Papers:
      - Final program report: papers/final-report.md
      - Publishable draft: papers/publishable.md
  - Simulations: simulations/overview.md
  - Glossary: glossary.md
  - Progress: progress.md
```

**Project-site path:** set `site_url` with trailing repo path; Material/MkDocs `use_directory_urls` defaults are fine if links are relative.

### 5.3 Sync script responsibilities

`scripts/sync_site_docs.py` should:

1. Read an allowlist table (path_in → path_out).
2. Copy files into `docs/...` (overwrite generated paths only).
3. Optionally rewrite **relative links** from research-tree paths to site paths (hardest part — phase this):
   - **Phase 1:** accept broken deep links; rely on nav + GitHub “view source on repo”.
   - **Phase 2:** automated link map for high-traffic pages (FINAL, claims).
4. Copy selected figures.
5. Exit non-zero if a source is missing.

Do **not** auto-sync denylisted trees.

### 5.4 Root `README.md` rewrite (dual audience)

Current root README is marked historical/superseded for the definition and is not a good public landing.

Plan:

| Audience | File |
|----------|------|
| **GitHub repo visitors** | Root `README.md` — short pitch, non-claims, link to live site + “read in repo” map |
| **Site visitors** | `docs/index.md` — polished narrative entry |

Both must link: canonical definition, master equation, FINAL report, non-claims.

### 5.5 What **not** to restructure yet

- Do not mass-delete root `*.markdown` or `drafts/` without explicit user confirmation (existing archive policy).
- Do not move `foundations/` or `emergent-gravity/` solely for Pages — copy/sync into `docs/`.
- Do not restart heat/PM dual research as part of “site polish.”

---

## 6. CI / deploy workflow

### 6.1 Workflow outline (`.github/workflows/pages.yml`)

```yaml
# Conceptual — implement later
name: Deploy GitHub Pages
on:
  push:
    branches: [master]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: pip install -r requirements-docs.txt
      - run: python scripts/sync_site_docs.py
      - run: mkdocs build --strict   # strict optional once links clean
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

### 6.2 One-time GitHub UI steps (manual)

1. Repo → **Settings → Pages**.
2. **Build and deployment → Source:** **GitHub Actions** (not “Deploy from a branch”).
3. Ensure Actions are enabled for the repo.
4. After first green run, verify `https://cyotee.github.io/computational-entropy/`.
5. Optional: add a repo badge / About → Website URL.

### 6.3 Local preview

```bash
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/python scripts/sync_site_docs.py
.venv/bin/mkdocs serve
# → http://127.0.0.1:8000
```

### 6.4 `.gitignore` additions

```gitignore
site/
docs/_generated/   # if using a generated subdirectory
```

(Only ignore pure build output; committed `docs/` landing pages stay tracked.)

---

## 7. Phased implementation

### Phase 0 — Preconditions (½ day)

- [ ] Confirm repo is **public**.
- [ ] Confirm no secrets in paths that might be copied (API keys, private notes).
- [ ] Decide Style **S1** (allowlist sync) vs S2.
- [ ] Decide primary paper page: `FINAL.md` vs `PUBLISHABLE.md` vs both.

### Phase 1 — Scaffold (1 day)

- [ ] Add `mkdocs.yml`, `requirements-docs.txt`, empty `docs/index.md`, math loader.
- [ ] Add `scripts/sync_site_docs.py` with **P0 allowlist only**.
- [ ] Local `mkdocs serve`; fix math on definition + master equation.
- [ ] Add `site/` to `.gitignore`.

### Phase 2 — Core narrative (1–2 days)

- [ ] Write public `docs/index.md`, `how-to-read.md`, `non-claims.md`.
- [ ] Sync foundations, master equation, claims, conclusions, FINAL/PUBLISHABLE.
- [ ] Glossary + progress (trim agent-only sections if needed).
- [ ] Rewrite root `README.md` with site link + short map.
- [ ] Nav complete for P0–P1.

### Phase 3 — Deploy (½ day)

- [ ] Add `.github/workflows/pages.yml`.
- [ ] Settings → Pages → GitHub Actions.
- [ ] Push; verify live URL, math CDN, 404s on nav links.
- [ ] Fix `site_url` / absolute asset paths if base path wrong under `/computational-entropy/`.

### Phase 4 — Hardening (ongoing)

- [ ] Link rewriting for top pages; turn on `mkdocs build --strict` when feasible.
- [ ] Embed 2–4 figures (scorecards) with captions and honesty labels.
- [ ] Optional: search boost, dark mode polish, citation CSS.
- [ ] Optional: host `PAPER.pdf` / HTML export under `docs/assets/` (self-authored only).
- [ ] Optional: custom domain.

### Phase 5 — Out of scope unless requested

- Full [PLAN.md](PLAN.md) research reorg.
- Publishing full simulation suite as interactive apps.
- Academic journal submission pipeline (see paper `PUBLISHING.md`).
- Rehosting external GfE PDFs.

---

## 8. Link and path strategy

| Problem | Approach |
|---------|----------|
| Repo-relative links in FINAL (`synthesis/...`) | Phase 1: leave as-is (may 404 on site); Phase 2: rewrite map in sync script |
| “View on GitHub” | Material `repo_url` + optional per-page source link to **canonical** path in monorepo |
| Images | Copy allowlisted PNGs into `docs/simulations/figures/` |
| PDFs we author | Place under `docs/assets/` or link raw GitHub |
| External literature | arXiv / DOI links only |

---

## 9. Risk register

| Risk | Mitigation |
|------|------------|
| Publishing superseded or over-claiming text | Landing non-claims; prefer CURRENT_CLAIMS + FINAL; avoid root historical README as theory authority |
| Copyright on external PDFs | Denylist PDFs; link arXiv |
| Broken math | Test arithmatex early on definition.md |
| Double maintenance of docs | Sync from canonical paths; never edit only the site copy of theory |
| `base` URL wrong on project Pages | Set `site_url` correctly; test on live host not only `localhost` |
| Strict build fails on incomplete links | Start without `--strict`; tighten later |
| Agent docs accidentally published | Allowlist-only sync; denylist CLAUDE/PRD/drafts |

---

## 10. Acceptance checklist (definition of done)

- [ ] Live site at `https://cyotee.github.io/computational-entropy/`
- [ ] Math renders on definition + master equation + at least one paper page
- [ ] Nav covers foundations → gravity → claims → report
- [ ] Non-claims visible without hunting
- [ ] CI deploys on push to `master`
- [ ] Root README points humans to the site
- [ ] No external copyrighted PDFs in the deployed artifact
- [ ] Canonical research paths unchanged for agents (`foundations/`, `emergent-gravity/`, `synthesis/`)

---

## 11. Suggested first implementation PR sequence

1. **PR1:** Scaffold (`mkdocs.yml`, `docs/index.md`, deps, gitignore, local serve works).
2. **PR2:** Sync script + P0 content + public non-claims/how-to-read.
3. **PR3:** GitHub Actions + Pages enablement + README site link.
4. **PR4:** Figures, link rewrites, more synthesis pages, `--strict` cleanup.

---

## 12. References (external)

- [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Material for MkDocs — Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)
- [MkDocs — Deploying your docs](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- In-repo: [papers/06-synthesis/PUBLISHING.md](papers/06-synthesis/PUBLISHING.md) (math + standalone paper constraints)

---

## 13. Decision log (fill in when implementing)

| Decision | Choice | Date |
|----------|--------|------|
| SSG | MkDocs Material (planned) | |
| Deploy method | GitHub Actions + Pages artifact (planned) | |
| Sync style | S1 allowlist copy (planned) | |
| Primary paper on site | TBD: FINAL / PUBLISHABLE / both | |
| Public PROGRESS_REPORT | Full vs trimmed | |

---

*This plan is implementation guidance only. No site files or workflows are required until a follow-up session executes Phase 1+.*
