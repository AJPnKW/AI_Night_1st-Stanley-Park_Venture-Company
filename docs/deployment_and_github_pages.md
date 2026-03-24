# Deployment And GitHub Pages

The site is ready for GitHub Pages because it is plain static content with no required build step.

Deployment notes:

- use `web/` as the standard editing/reference folder
- publish from the `github/` folder content, which mirrors `web/`
- ensure the configurable form endpoint in `github/assets/js/site.js` is updated before collecting live approvals
- test print output and the consent fallback before event use

If the repository is later connected to Pages with a custom workflow, keep the output identical to the current static file structure.
