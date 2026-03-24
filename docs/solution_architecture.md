# Solution Architecture

The solution is a no-build static site rooted at `AI_Workshop_4_ventures/web/`, with a mirrored publishable copy in `github/`.

- Shared assets live in `AI_Workshop_4_ventures/web/assets/`
- Public pages live in `AI_Workshop_4_ventures/web/index.html`, `AI_Workshop_4_ventures/web/participant/`, `AI_Workshop_4_ventures/web/parent/`, `AI_Workshop_4_ventures/web/shared/`, and `AI_Workshop_4_ventures/web/legal/`
- Low-profile pages live in `AI_Workshop_4_ventures/web/leader/` and `AI_Workshop_4_ventures/web/facilitator/`
- Documentation lives in `docs/`
- Reports live in `reports/`
- Repeatable QA scripts live in `scripts/`

JavaScript is intentionally limited to navigation behavior, active-link highlighting, footer year injection, and form-endpoint configuration. The consent flow supports static hosting by using a configurable third-party form handler endpoint and a printable fallback.
