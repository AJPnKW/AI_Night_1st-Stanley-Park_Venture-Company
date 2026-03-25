# Technical Structure

Standard site root: `AI_Workshop_4_ventures/web/`

Publish mirror: `github/`

Authoritative structure contract:

- `docs/structure_and_responsibility_model.md`

- `AI_Workshop_4_ventures/web/assets/css/site.css`: shared styles
- `AI_Workshop_4_ventures/web/assets/css/print.css`: print behavior
- `AI_Workshop_4_ventures/web/assets/js/site.js`: mobile navigation, active links, role access, form workflow logic, local draft capture, print/download helpers
- `AI_Workshop_4_ventures/web/assets/images/`: branding hooks
- `AI_Workshop_4_ventures/web/access/`: common role-access entry point
- `AI_Workshop_4_ventures/web/participant/`, `AI_Workshop_4_ventures/web/parent/`, `AI_Workshop_4_ventures/web/shared/`, `AI_Workshop_4_ventures/web/legal/`: public workflow pages
- `AI_Workshop_4_ventures/web/leader/`, `AI_Workshop_4_ventures/web/facilitator/`: low-profile execution/support pages

Project support folders:

- `docs/`: living documentation
- `reports/`: inventory, architecture, QA, deployment, summary artifacts
- `scripts/`: repeatable QA and packaging scripts
- `logs/`, `out/`: run outputs created by scripts
