# Form And Data Handling Decision Record

Decision: use a static-site-compatible third-party form handler pattern with a configurable endpoint in `AI_Workshop_4_ventures/web/assets/js/site.js`.

Why:

- works with GitHub Pages
- avoids building a backend
- supports minimal data collection
- can be disabled until ready

Fallback:

- printable approval capture using the same minimum field set

Controls:

- minimal fields only
- organizer-controlled contact details
- delete collected records after short event follow-up
