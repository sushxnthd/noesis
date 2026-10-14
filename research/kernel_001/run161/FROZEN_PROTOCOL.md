# Run 161 — FROZEN prospective held-out ray-repair coverage

Frozen before running the Run 161 evaluation. Parent: research/kernel-001-run160-boundary-quotient. No changes to trained weights before evaluation.

## Primary question
Does the Run 160 one-coordinate task-quotient repair, without hand-picking a coordinate or seed, certify a substantial fraction of previously archived but not previously used-for-repair Adam-trained recurrent counters?

## Held-out population
Exactly 14 archived Run 154B checkpoints: seeds 224 and 226–238 inclusive (exclude 225, previously investigated). These weights are held out from Run 160 repair development. They are not a new independent training cohort and this is not a prospective *training* study. Source: NOESIS_kernel001_run154_frozen_cycle_negative.tar.gz, CHECKPOINT_SEED_*.json. Freeze their SHA256 hashes before examining results.

## Frozen algorithm
Interpret every JSON floating-point parameter string as an exact decimal rational. For each candidate coordinate k=0,...,d-1, require A[k,k]=1, E[0,k]>0, and for all j!=k: A[j,k]<=0 and E[0,j]<=0. Construct exact one-ray projection by replacing E[1,k]=-E[0,k], E[2,k]=0, w[k]=1/E[0,k], and setting positive off-ray E[1,j], E[2,j] to zero. Do not change A or E[0]. Require all post-projection off-ray inequalities, exact rational all-alphabet induction, <=6 scalar changes, and max absolute scalar edit <=1e-6. If several k qualify, choose the minimum edit count, then minimum maximum edit, then smallest k. If none qualify, mark failure/ineligible, never remove it from denominator. No gradient fine-tuning or task-aware seed exclusions.

## Scalar success criterion
At least 7 of 14 held-out models certified with <=6 scalar edits and max |delta| <=1e-6. Primary statistic: certified count / 14.

## Strongest competing explanation
This projects task semantics into an already nearly one-ray architecture. It demonstrates sparse repairability, not autonomous algorithm acquisition or general model-agnostic certification.

## Cheapest decisive falsification
Any exact-rational word violating h=u*c*e_k after repair; or <7/14 qualifying checkpoints; or a checker disagreement. Independently implement the proof and exhaustive length-6 test.

## Publishable threshold
Frozen >1 architecture/task-family and independently trained checkpoints, adversarial cap spoof, statistically characterized repair coverage, priority audit, and evidence of algorithm acquisition transitions without injecting task semantics.

## Learning relevance threshold
Weights must be archived Adam-trained, with before/after exact-rational witnesses, and repair fraction reported with all failures. No claims about new training transitions.

## Kill condition
If <3/14 qualify or an inductive proof fails, retire the narrow one-ray sparse-repair diagnostic; otherwise if 3–6 qualify, retain only as a low-coverage method and reformulate after at most two more substantive failures.

## Provenance
All source files, per-checkpoint SHA256 hashes, raw decisions, edits, exact tests, independent checker, failures, and THEORY/LEARNING ledgers must be persisted on this research branch. Do not merge into main.
