# AI Night: 1st Stanley Park Venture Company

<p align="center">
  <img src="AI_Workshop_4_ventures/web/assets/icons/favicon.svg" alt="AI Night icon" width="72" height="72">
</p>

<p align="center"><strong>Browser-first workshop site and delivery system for a guided introductory AI night.</strong></p>
<p align="center">Independent volunteer support project for one event. This is not an official Scouts Canada or group-owned website.</p>

<p align="center">
  <a href="https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/"><img src="https://img.shields.io/badge/live%20site-GitHub%20Pages-0f4c81?style=for-the-badge" alt="Live site badge"></a>
  <img src="https://img.shields.io/badge/model-browser--first-1d7a85?style=for-the-badge" alt="Browser-first badge">
  <img src="https://img.shields.io/badge/status-production%20ready-2f7a4a?style=for-the-badge" alt="Production ready badge">
</p>

---

## Hero

This repository powers a calm, low-friction introduction to AI and ChatGPT for Scouts and Venturers. The active public experience is browser-first, with guided prompt practice, exercises, reflections, and role-based support pages for participants, families, leaders, and facilitators.

GitHub Pages is the canonical public front end. Interactive workbook behavior runs client-side in the browser, while structured pre-event and feedback collection are designed around organizer-issued Google Forms.

## Quick Start

| Start here | Destination |
| --- | --- |
| Live site | [Open the public site](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/) |
| Participant guide | [Youth page](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/participant/index.html) |
| Parent guide | [Parent guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/parent/index.html) |
| Leader guide | [Leader guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/leader/index.html) |
| Facilitator run-of-show | [Run of show](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/facilitator/run-of-show.html) |
| Exercises | [Exercises](github/participant/exercises.html) |
| Reflection workbook | [Reflections](github/participant/reflections.html) |
| Knowledge base | [KB and references](github/kb/index.html) |
| Project dashboard | [Coordination dashboard](AI_Workshop_4_ventures/docs/project_coordination_dashboard.html) |

## Role-Based Navigation

| Role | Best page | What it covers |
| --- | --- | --- |
| Youth participant | [Participant guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/participant/index.html) | What to bring, how the session works, exercises, reflections |
| Parent or guardian | [Parent guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/parent/index.html) | Browser-first expectations, trust layer, privacy and fallback notes |
| Leader | [Leader guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/leader/index.html) | Support role, logistics, fallback handling, escalation cues |
| Facilitator | [Facilitator run-of-show](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/facilitator/run-of-show.html) | Live sequence, demo prompts, recovery notes |
| Repo/operator view | [Project dashboard](AI_Workshop_4_ventures/docs/project_coordination_dashboard.html) | Build status, validation, coordination docs, packaging evidence |

## Live Site

The public site is the main front door:

- [Live site](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/)
- [Participant guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/participant/index.html)
- [Parent guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/parent/index.html)
- [Leader guide](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/leader/index.html)
- [Facilitator run-of-show](https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company/facilitator/run-of-show.html)
- [Exercises](github/participant/exercises.html)
- [Reflection workbook](github/participant/reflections.html)
- [Knowledge base](github/kb/index.html)

## What This Project Supports

- Browser-first AI night delivery for mixed-comfort participants
- Guided prompt practice with weak-vs-strong comparisons
- Parent and guardian trust-layer content
- Role-specific public pages for youth, parents, leaders, and facilitators
- Exercises, reflections, and printable takeaways
- Knowledge and reference content to support safer, more confident use
- GitHub Pages for the public front end plus Google Forms for structured survey collection

## What Participants, Parents, and Leaders Should Do

| Audience | What to do |
| --- | --- |
| Participants | Open the participant guide, bring a charger, and use the browser-first path |
| Parents or guardians | Read the parent guide and review account and shared-device choices as a family |
| Leaders | Use the leader guide and keep support focused on access, pacing, and fallback routing |
| Facilitators | Open the run-of-show, exercises, reflections, and KB before the session starts |

## What Is Not Required by Default

- No local VM is required
- No coding tools are required
- No advanced local installs are required
- No terminal workflow is required for participants

## What This Repo Contains

| Area | Purpose |
| --- | --- |
| [`AI_Workshop_4_ventures/web/`](AI_Workshop_4_ventures/web/) | Canonical working public site content |
| [`AI_Workshop_4_ventures/docs/`](AI_Workshop_4_ventures/docs/) | Coordination, facilitator, communications, survey, and status docs |
| [`AI_Workshop_4_ventures/scripts/`](AI_Workshop_4_ventures/scripts/) | Build, sync, archive, readiness, validation, and packaging scripts |
| [`AI_Workshop_4_ventures/artifacts/`](AI_Workshop_4_ventures/artifacts/) | Machine-readable build, readiness, validation, and archive outputs |
| [`AI_Workshop_4_ventures/reports/`](AI_Workshop_4_ventures/reports/) | Human-readable HTML reports |
| [`github/`](github/) | GitHub Pages publish mirror used by the deploy workflow |

## Project Structure Snapshot

| Layer | Active location | Notes |
| --- | --- | --- |
| Public site content | `AI_Workshop_4_ventures/web/` | Browser-first public pages and role guides |
| Docs | `AI_Workshop_4_ventures/docs/` | Operator, facilitator, planning, and status material |
| Scripts | `AI_Workshop_4_ventures/scripts/` | Deterministic build and validation tooling |
| Reports and artifacts | `AI_Workshop_4_ventures/reports/`, `AI_Workshop_4_ventures/artifacts/` | Validation evidence and generated reports |
| Publish mirror | `github/` | Deployed to GitHub Pages via workflow |

## Project Status

- Browser-first model is normalized and active
- Public pages for participants, parents, leaders, and facilitators are present
- Exercises and reflection workbook are present
- Knowledge base and reference pages are present
- Packaging, archive rationalization, and validation are present
- Google Forms is the canonical survey strategy, but organizer-owned live form URLs are intentionally managed outside the public repo

Useful repo-side references:

- [Validation status](AI_Workshop_4_ventures/docs/current_state_validated_vs_unvalidated.html)
- [Workshop architecture](AI_Workshop_4_ventures/docs/workshop_delivery_architecture.html)
- [Parent information pack](AI_Workshop_4_ventures/docs/parent_information_pack.html)
- [Presenter operations pack](AI_Workshop_4_ventures/docs/presenter_operations_pack.html)
- [Backup facilitator pack](AI_Workshop_4_ventures/docs/backup_facilitator_pack.html)
- [Platform capabilities and limits](AI_Workshop_4_ventures/docs/platform_capabilities_and_limits.html)
- [Forms and backend supplement plan](AI_Workshop_4_ventures/docs/forms_and_backend_supplement_plan.html)

## Important Notes

- This is an independent volunteer support repository for one workshop event.
- Public informational pages are intended for participants, families, and leaders.
- Internal or protected areas may exist operationally; passwords or access credentials are not published here.
- The live public destination is GitHub Pages. The working source is `AI_Workshop_4_ventures/web/`, and the deploy mirror is `github/`.
- Where a freshly generated detail page is not yet visible on GitHub Pages, this README links to the canonical repo-side publish mirror rather than a broken live route.
- Workbook notes stay local to the participant browser by default. Structured surveys and feedback use organizer-issued Google Forms outside the public site.
