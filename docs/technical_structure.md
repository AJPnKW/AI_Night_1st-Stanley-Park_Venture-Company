# Technical Structure

Standard site root: `web/`

Publish mirror: `github/`

- `web/assets/css/site.css`: shared styles
- `web/assets/css/print.css`: print behavior
- `web/assets/js/site.js`: mobile navigation, active links, year, form config
- `web/assets/images/`: branding hooks
- `web/participant/`, `web/parent/`, `web/shared/`, `web/legal/`: public pages
- `web/leader/`, `web/facilitator/`: low-profile direct-link pages

Project support folders:

- `docs/`: living documentation
- `reports/`: inventory, architecture, QA, deployment, summary artifacts
- `scripts/`: repeatable QA and packaging scripts
- `logs/`, `out/`: run outputs created by scripts
