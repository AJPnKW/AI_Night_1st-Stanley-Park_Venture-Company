# Structure And Responsibility Model

Date: 2026-03-24

## Authoritative Paths

- Project container root:
  - `C:\Users\andrew\PROJECTS\Scouter_Jenn`
- Implementation workspace root:
  - `C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures`
- Canonical editable website source:
  - `C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures\web`
- Publish mirror:
  - `C:\Users\andrew\PROJECTS\Scouter_Jenn\github`

## Responsibility Rules

- All website design, content, UX, and workshop-system implementation belongs in:
  - `AI_Workshop_4_ventures\web`
- The `github/` folder is a synchronized publish mirror, not the primary authoring source.
- Parent-level repo files may be updated only for:
  - documentation
  - QA tooling
  - reporting
  - deployment workflow
  - packaging
  - mirror-sync support

## Read / Modify Scope

Codex may read:

- parent-level docs, reports, scripts, workflows, README
- child-level workshop materials, source pages, assets, pulled references, scripts, and packs

Codex may modify:

- `AI_Workshop_4_ventures\web`
- `github`
- parent-level docs, reports, scripts, and deployment/QA support files when required

Codex should not:

- create a parallel site root
- move implementation into the parent root
- treat `github/` as the design source
- drift content between roots without synchronizing the mirror

## Practical Working Model

1. Edit canonical pages in `AI_Workshop_4_ventures\web`.
2. Sync those changes into `github/`.
3. Run QA against both roots.
4. Commit only after canonical and mirror are aligned.

## Workshop-System Interpretation

This repo is not only a static website project.

It is a workshop learning-delivery system implemented through:

- the website
- facilitator execution references
- parent/privacy/consent guidance
- participant pre-work and live-session guidance
- leader support materials
- QA/reporting artifacts
