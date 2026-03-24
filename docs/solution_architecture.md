# Solution Architecture

The solution is a no-build static site rooted at `github/`.

- Shared assets live in `github/assets/`
- Public pages live in `github/index.html`, `github/participant/`, `github/parent/`, `github/shared/`, and `github/legal/`
- Low-profile pages live in `github/leader/` and `github/facilitator/`
- Documentation lives in `docs/`
- Reports live in `reports/`
- Repeatable QA scripts live in `scripts/`

JavaScript is intentionally limited to navigation behavior, active-link highlighting, footer year injection, and form-endpoint configuration. The consent flow supports static hosting by using a configurable third-party form handler endpoint and a printable fallback.

