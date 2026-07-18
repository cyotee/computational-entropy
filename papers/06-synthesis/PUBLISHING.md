# Publishing notes — math rendering & standalone structure

## 1. Why equations looked broken

The research draft `FINAL.md` used **LaTeX delimiters** `\(...\)` and `\[...\]`.

| Viewer | Typical behavior |
|--------|------------------|
| Many Markdown previews (basic GFM) | **Do not** render `\(`/`\[`; show raw backslashes |
| GitHub (newer) | Prefers `$...$` / `$$...$$` |
| Pandoc → PDF/HTML with MathJax | Both styles can work; `$`/`$$` is more portable |
| Nested math e.g. `\[ ... \(G\) ... \]` | **Breaks** some engines |

**Fix:** `PUBLISHABLE.md` converts all math to **`$...$` / `$$...$$`** and removes nested math mode inside displays.

**For PDF:** from repo root,

```bash
pandoc papers/06-synthesis/PUBLISHABLE.md -o papers/06-synthesis/PUBLISHABLE.pdf \
  --pdf-engine=xelatex -V geometry:margin=1in
# or:
pandoc papers/06-synthesis/PUBLISHABLE.md -o papers/06-synthesis/PUBLISHABLE.html --mathjax
```

If PDF fails, install a TeX engine or use HTML+MathJax for review.

---

## 2. Why repo file links are wrong for a published paper

Internal links like `synthesis/m11d-composition-laws.md` or `../../emergent-gravity/master-equation.md` only work **inside the git repo**. A published PDF is **standalone**: readers have no repo tree.

**What real papers do instead:**

| Instead of repo links… | Use… |
|------------------------|------|
| Core definitions / theorems used in the argument | **Main text** (self-contained) |
| Long proofs, tables, numerical protocols | **Appendices** |
| Prior *published* results (Jacobson, Bianconi, Landauer, Shannon, …) | **Bibliography citations** |
| Your own unpublished notes / code | **Data availability / supplementary repo** (optional URL), not inline hyperlinks as logic steps |

**Fix:** `PUBLISHABLE.md` strips repo paths/links and adds:

- **Appendix A** — constructive witnesses (AND, composition, Landauer, PM, dual toys, …)  
- **Appendix B** — claim / non-claim checklist  
- **Appendix C** — open mathematical avenues  
- **Bibliography** — published external works only  

Repo code remains the **reproducibility backend**, not part of the narrative chain.

---

## 3. Files

| File | Role |
|------|------|
| `FINAL.md` | Full research freeze (keeps repo links for agents) |
| **`PUBLISHABLE.md`** | **Standalone draft for human review / publish decision** |
| `PUBLISHING.md` | This note |

---

## 4. Still to do before submission (after you review content)

1. Author list, abstract word limit, venue style  
2. Pandoc/LaTeX polish (theorem environments, equation numbers, cross-refs)  
3. Embed 2–4 figures (scorecards / tables) as images, not “run this script”  
4. Expand bibliography with full bibliographic records (DOI/arXiv IDs)  
5. Optional: “Code and ledgers: available at [repo URL]” one-liner  

Content decision still rests on whether P1–P11 + appendices meet your bar without O1–O3 closed.
