# Deployment And GitHub Pages

The site is ready for GitHub Pages because it is plain static content with no required build step.

Deployment notes:

- use `AI_Workshop_4_ventures/web/` as the standard editing/reference folder
- publish from the `github/` folder content, which mirrors `AI_Workshop_4_ventures/web/`
- ensure the configurable form endpoint in `AI_Workshop_4_ventures/web/assets/js/site.js` is updated before collecting live approvals
- test print output and the consent fallback before event use

If the repository is later connected to Pages with a custom workflow, keep the output identical to the current static file structure.
