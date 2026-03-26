# AI Workshop Resource System

## Purpose

This parent-level document is the roll-up summary for the workshop resource system. The authoritative workshop resource workstream lives under:

- `C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures`

## Boundary Model

- Parent project root:
  - repo container
  - shared docs
  - reports
  - logs
  - deployment mirror support
- Workshop root:
  - downloaded sources
  - reference catalog
  - workshop scripts
  - workshop packs
  - canonical editable workshop website
- Published site root:
  - static deployable mirror only
  - no workshop pack logic, no source cache, no reference-catalog working files

## Authoritative Workshop Resource Locations

- Local references: `AI_Workshop_4_ventures\downloaded_sources`
- Resource catalog: `AI_Workshop_4_ventures\reference_catalog`
- Workshop automation: `AI_Workshop_4_ventures\scripts`
- Workshop pack artifacts: `AI_Workshop_4_ventures\workshop_pack`
- Canonical site content: `AI_Workshop_4_ventures\web`

## Learning Content Expansion

The expanded workshop learning-system content is maintained in the workshop root, not the parent root.

Primary maintained workshop-local files:

- `AI_Workshop_4_ventures\reference_catalog\learning_plan_expansion.md`
- `AI_Workshop_4_ventures\reference_catalog\slide_candidate_matrix.csv`
- `AI_Workshop_4_ventures\reference_catalog\slide_candidate_matrix.md`
- `AI_Workshop_4_ventures\reference_catalog\detailed_resource_inventory.csv`
- `AI_Workshop_4_ventures\reference_catalog\detailed_resource_inventory.md`

Expansion coverage includes:

1. validated source claims
2. slide candidate selection
3. expanded learning-plan guidance
4. consolidated activity, safe-use, Codex, and beginner-limits guidance inside one master workshop-local learning-plan file

Existing pack reuse strategy:

- preserve `workshop_pack` as the original artifact source
- crosswalk each existing file against current scope
- reuse valid structure where possible
- fill gaps with workshop-root documentation, not parent-root drift

## Validation Model

Authoritative workshop validation files:

- `AI_Workshop_4_ventures\reference_catalog\source_claim_validation.csv`
- `AI_Workshop_4_ventures\reference_catalog\source_claim_validation.md`

Validation standard:

- use at least two credible sources where possible
- prefer local cached sources before new downloads
- distinguish between factual validation and pedagogical validation
- mark partially validated teaching-pattern claims explicitly

## Parent-Level Role

The parent root should only carry workshop-related roll-up documentation, not the workshop-local source cache or planning corpus. This avoids repeating the earlier drift where parent-level structures were mistaken for the workshop authority.
