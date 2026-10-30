Research Methodology

1. Purpose

This document defines the experimental methodology for evaluating Meta-Graph Research.

The goal is to determine whether explicit reasoning dependencies, evidence-aware revision, and failure analysis improve reasoning reliability.

2. Research Approach

Use controlled comparative experiments.

Each proposed mechanism should initially be evaluated independently before testing combinations.

The research must distinguish measurable improvements from increased system complexity.

3. Experimental Conditions

The initial experiment EXP-001 will compare four conditions.

Condition A — Baseline

A reasoning system without explicit dependency tracking or evidence-aware revision.

Condition B — Dependency Tracking

The system explicitly represents relationships between claims, assumptions, evidence, and conclusions.

Condition C — Evidence-Aware Revision

The system evaluates evidence and revises affected conclusions when new information becomes available.

Condition D — Failure Pattern Analysis

The system analyzes recurring failures and proposes potential improvements.

Structural changes must be evaluated separately and must not be assumed beneficial.

4. Benchmark Design

Create a controlled benchmark containing tasks with known reasoning conditions.

Include:

* Missing evidence.
* Contradictory evidence.
* False assumptions.
* New evidence invalidating previous conclusions.
* Multiple conclusions depending on one assumption.
* Misleading sources.
* Incorrect failure diagnoses.
* Revision-induced regressions.
* Repeated reasoning failures.
* Cases where uncertainty is the correct answer.

Each task must have a documented expected outcome and evaluation criteria.

5. Experimental Procedure

For each experiment:

1. Record the research question.
2. Define the hypothesis.
3. Record the system configuration.
4. Fix the evaluation criteria.
5. Execute the baseline.
6. Execute the experimental condition.
7. Save raw outputs.
8. Evaluate results.
9. Analyze failures.
10. Document limitations.

6. Evaluation Metrics

Accuracy

Proportion of correct conclusions.

Failure Detection Rate

Proportion of planted reasoning failures successfully detected.

Unsupported Conclusion Rate

Proportion of conclusions that lack sufficient justification.

Diagnosis Accuracy

Proportion of failures for which the underlying cause is correctly identified.

Dependency Tracing Accuracy

Proportion of affected dependencies correctly identified.

Recovery Accuracy

Proportion of invalid conclusions successfully corrected.

Regression Rate

Frequency of previously correct conclusions becoming incorrect after revision.

Generalization

Performance on cases not used during development.

Computational Cost

Resources and time required to execute reasoning and revision.

7. Experimental Controls

Where possible, keep constant:

* Model version.
* Dataset.
* Task difficulty.
* Prompt structure.
* Evaluation criteria.
* Random seed.
* Computational environment.

Any unavoidable differences must be documented.

8. Reproducibility

Every experiment must preserve:

* Experiment ID.
* Dataset version.
* Code commit.
* Model identifier.
* Configuration.
* Random seed.
* Raw outputs.
* Evaluation results.
* Execution environment.
* Known limitations.

9. Statistical Evaluation

Use appropriate statistical comparisons when sufficient observations are available.

Report:

* Sample size.
* Mean and variance where applicable.
* Confidence intervals where appropriate.
* Effect sizes.
* Uncertainty.
* Failed and inconclusive results.

Do not claim statistical significance without an appropriate analysis.

10. Failure Analysis

When a system fails, determine:

1. Was the failure detected?
2. Was the correct cause identified?
3. Were the relevant dependencies traced?
4. Was the revision justified by evidence?
5. Did the revision introduce regressions?
6. Did the system learn anything generalizable?

11. Research Integrity

* Preserve raw experimental data.
* Never fabricate results.
* Never silently modify evaluation criteria.
* Separate exploratory and confirmatory experiments.
* Report negative results.
* Do not confuse correlation with causation.
* Do not equate longer explanations with better reasoning.

12. Status

This methodology is provisional.

It must be refined after the related-work review and before running confirmatory experiments.
