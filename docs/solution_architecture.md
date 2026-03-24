# Solution Architecture

The solution is a no-build static site rooted at `web/`, with a mirrored publishable copy in `github/`.

- Shared assets live in `web/assets/`
- Public pages live in `web/index.html`, `web/participant/`, `web/parent/`, `web/shared/`, and `web/legal/`
- Low-profile pages live in `web/leader/` and `web/facilitator/`
- Documentation lives in `docs/`
- Reports live in `reports/`
- Repeatable QA scripts live in `scripts/`

JavaScript is intentionally limited to navigation behavior, active-link highlighting, footer year injection, and form-endpoint configuration. The consent flow supports static hosting by using a configurable third-party form handler endpoint and a printable fallback.
