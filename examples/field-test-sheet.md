# R2R field-test worksheet — evidence before advocacy

A simple sheet for **future** real deployments. Do not fill unobserved fields with estimates or model assertions.

## Setup

| Field | Record |
| --- | --- |
| Product and repo (share only with rights) | |
| Task scope and user journey | |
| Current spec + acceptance baseline | |
| Model/agent version and tooling | |
| Developer/reviewer role and permission scope | |
| A: baseline method | |
| B: R2R method | |
| Comparison constraints and deviations | |

## During each run

| Timestamp | Method | Meaningful accepted user outcome | Agent wall time | Human time | Review wait | Rework | Evidence SHA / artifact |
| --- | --- | --- | --- | --- | --- | --- | --- |

## At final acceptance

| Question | A | B |
| --- | --- | --- |
| Real end-to-end journey passed? | NOT_RUN | NOT_RUN |
| Important negative cases tested? | NOT_RUN | NOT_RUN |
| Release quality met at matched scope? | UNVERIFIED | UNVERIFIED |
| Unresolved P0/P1? | UNKNOWN | UNKNOWN |
| Total elapsed duration? | NOT_MEASURED | NOT_MEASURED |
| Total model and infrastructure cost? | NOT_MEASURED | NOT_MEASURED |
| Human review time? | NOT_MEASURED | NOT_MEASURED |
| Architecture rework cost? | NOT_MEASURED | NOT_MEASURED |

Never interpret placeholder statuses as measured results. See [evaluation protocol](../docs/research/evaluation-protocol.md) and [research hypotheses](../docs/research/problem-and-hypotheses.md).
