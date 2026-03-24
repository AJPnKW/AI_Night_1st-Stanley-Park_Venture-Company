# QA Results

Recorded executions:

- `20260324_122141`: `github/` pass, 17 HTML files checked, 0 missing links, 0 content issues, 0 warnings
- `20260324_143650`: top-level `web/` pass and `github/` mirror pass, 17 HTML files checked in each path, 0 missing links, 0 content issues, 0 warnings
- `20260324_150305_417`: canonical `AI_Workshop_4_ventures/web/` pass, 17 HTML files checked, 0 missing links, 0 content issues, 0 warnings
- `20260324_150319_893`: `github/` publish mirror pass after canonical-path cleanup, 17 HTML files checked, 0 missing links, 0 content issues, 0 warnings

Detailed run artifacts are written by `scripts/qa_site.ps1` into `reports/runs/<timestamp>/qa_results.md` and bundled into `out/<timestamp>/`.
