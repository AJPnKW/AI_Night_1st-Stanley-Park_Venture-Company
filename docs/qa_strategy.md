# QA Strategy

The QA pass checks:

- internal link integrity
- missing file references
- missing titles and `h1`
- disclaimer presence on required pages
- placeholder and banned text scans
- stale `24th` references
- print stylesheet presence
- basic documentation alignment

QA is automated with `scripts/qa_site.ps1`, which creates timestamped output folders and a zip bundle.

