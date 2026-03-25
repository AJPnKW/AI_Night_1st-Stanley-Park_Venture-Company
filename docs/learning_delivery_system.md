# Learning Delivery System

Date: 2026-03-24

## Purpose

The website now acts as a workshop learning-delivery system, not only a brochure site.

It supports:

- pre-work
- participant readiness
- parent understanding and approval
- leader room/support coordination
- facilitator live delivery
- post-session follow-up

## Learning System Layers

### Layer 1. Scaffolded Learning

- early success in the first 15 to 20 minutes
- simple language
- visible structure
- one-step-at-a-time instructions
- practical examples before independent work

### Layer 2. Execution Engine

- facilitator-facing run-of-show
- shared five-step workshop model
- participant-visible sequence
- timing bundles and live transitions

### Layer 3. Adaptive Support

- fast-learner extension paths
- slower-learner fallback paths
- stuck/recovery prompts
- explicit low-pressure support cues
- neurodivergent-friendly predictability

### Layer 4. Support Platform

- landing page as front door
- sign-up and waiver workflows
- participant portal
- parent pages
- leader page
- facilitator page and run-of-show

### Layer 5. Data Feedback Loop

- minimal readiness data
- facilitator-facing interpretation of that data
- no unnecessary personal data collection
- clear explanation of why readiness information is requested

## 90-Minute System Model

- `0–5 min`: arrival, settle in, device/Wi-Fi check
- `5–10 min`: AI framing, expectations, privacy/safety
- `10–15 min`: demo with visible useful outcome
- `15–20 min`: common first task
- `20–30 min`: select project pathway
- `30–45 min`: build block 1
- `45–60 min`: build block 2 with recovery paths
- `60–75 min`: refine / polish / extend
- `75–85 min`: share-back / reflection
- `85–90 min`: close and next-step guidance

## Where The System Lives

- landing and workflow front door:
  - `AI_Workshop_4_ventures/web/index.html`
- participant workflow:
  - `AI_Workshop_4_ventures/web/participant/`
- parent workflow:
  - `AI_Workshop_4_ventures/web/parent/`
- facilitator live-use materials:
  - `AI_Workshop_4_ventures/web/facilitator/`
- leader support:
  - `AI_Workshop_4_ventures/web/leader/`

## Current Limits

- role access is client-side convenience gating, not secure authentication
- centralized form collection still depends on configuring an external endpoint
