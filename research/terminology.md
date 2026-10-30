Research Terminology

1. Purpose

This document establishes a shared vocabulary for Meta-Graph Research.

All research agents, experiments, documentation, and implementations should use these definitions consistently.

2. Core Knowledge Elements

Claim

A statement proposed as potentially true.

A claim may be supported, unsupported, uncertain, or contradicted.

Evidence

Information used to support or challenge a claim.

Evidence must have an identifiable origin whenever possible.

Source

The origin from which evidence was obtained.

Sources may differ in reliability, relevance, independence, and limitations.

Assumption

A proposition temporarily accepted for the purpose of reasoning without sufficient direct verification.

Assumptions must be explicitly identified.

Inference

A reasoning operation that derives a conclusion from claims, evidence, assumptions, and inference rules.

Conclusion

A claim produced or accepted as the result of reasoning.

Inference Rule

A formal or operational rule governing how conclusions are derived from premises.

3. Relationships

Dependency

A relationship indicating that one claim or conclusion relies on another claim, assumption, evidence item, or inference rule.

Reasoning Dependency Graph

A structured representation of claims and the relationships that support or influence them.

Provenance

The recorded origin and history of a claim, evidence item, or conclusion.

Justification

The explicit reasons and dependencies supporting a conclusion.

4. Failure and Uncertainty

Contradiction

A situation in which two or more claims cannot all be true under the same interpretation and conditions.

A contradiction does not automatically establish which claim is false.

Unsupported Conclusion

A conclusion that lacks sufficient evidence or valid justification.

Reasoning Failure

An error or limitation in the process of deriving, evaluating, or revising conclusions.

Failure Diagnosis

The process of identifying the cause and location of a reasoning failure.

Root Cause

An underlying condition, assumption, dependency, or reasoning operation responsible for a failure.

Uncertainty

A state in which available information does not justify a sufficiently confident conclusion.

Uncertainty must not be confused with falsity.

5. Revision and Adaptation

Claim Revision

Changing the status or content of an individual claim based on new information or identified errors.

Dependency Revision

Revising conclusions and relationships affected by a changed assumption, claim, or evidence item.

Revision History

A persistent record of previous conclusions, their justifications, and the reasons for revision.

Failure Pattern

A recurring structure or cause observed across multiple reasoning failures.

Structural Adaptation

A proposed change to the reasoning system’s architecture, rules, or dependency representation in response to identified failure patterns.

Regression

A situation in which a change improves some outcomes but makes previously successful outcomes worse.

6. Evidence Quality

Evidence should be evaluated using the following dimensions:

* Source reliability.
* Relevance.
* Directness.
* Recency.
* Independence.
* Consistency with other evidence.
* Known limitations.

No single confidence score should replace the underlying evidence record.

7. Three Levels of Revision

L1 — Claim Revision

Correction of an individual conclusion.

L2 — Dependency Revision

Identification and correction of other conclusions affected by the revision.

L3 — Structural Adaptation

Identification of recurring failures and evaluation of proposed architectural changes.

8. Research Data Principle

The system should distinguish between:

* What is known.
* What is observed.
* What is inferred.
* What is assumed.
* What is disputed.
* What remains unknown.

These categories must not be silently merged.

9. Status

This terminology is an initial working specification.

Definitions may evolve as the literature review and experiments reveal the need for more precise distinctions.
