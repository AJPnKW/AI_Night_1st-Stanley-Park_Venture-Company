# Maintenance Guide

For non-developer maintenance:

- edit the HTML files directly in `web/`
- mirror approved site changes into `github/` before publish
- replace `web/assets/images/branding-placeholder.svg` when a better event image is available
- update the form handler settings in `web/assets/js/site.js`
- run `scripts/qa_site.ps1` after content changes
- review generated reports under `reports/runs/`

When changing content, keep the independence disclaimer intact and avoid adding extra data fields unless there is a clear event need.
