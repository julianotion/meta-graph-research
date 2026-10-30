Evaluation Metrics

1. Purpose

This document defines measurable criteria for evaluating reasoning reliability, failure diagnosis, evidence-aware revision, and structural adaptation.

All metrics must be calculated using documented evaluation procedures.

2. Core Metrics

2.1 Answer Accuracy

Percentage of tasks for which the final conclusion matches the expected outcome.

Formula:

Accuracy = Correct Conclusions / Total Evaluated Conclusions

2.2 Failure Detection Rate

Percentage of deliberately introduced reasoning failures successfully detected.

Formula:

Detection Rate = Detected Failures / Total Introduced Failures

2.3 Unsupported Conclusion Rate

Percentage of conclusions that lack sufficient supporting evidence or valid justification.

Formula:

Unsupported Rate = Unsupported Conclusions / Total Conclusions

2.4 Diagnosis Accuracy

Percentage of detected failures for which the underlying cause is correctly identified.

Formula:

Diagnosis Accuracy = Correct Diagnoses / Total Evaluated Diagnoses

2.5 Dependency Tracing Accuracy

Percentage of relevant dependencies correctly identified during failure analysis.

Formula:

Tracing Precision = Correctly Identified Relevant Dependencies / All Identified Relevant Dependencies

Tracing Recall = Correctly Identified Relevant Dependencies / All Relevant Dependencies

2.6 Recovery Accuracy

Percentage of invalid conclusions successfully corrected after revision.

Formula:

Recovery Accuracy = Correctly Recovered Conclusions / Total Conclusions Requiring Recovery

2.7 Regression Rate

Percentage of previously correct conclusions that become incorrect after revision.

Formula:

Regression Rate = Previously Correct Conclusions Made Incorrect / Total Previously Correct Conclusions Re-evaluated

2.8 False-Positive Revision Rate

Percentage of revisions applied to conclusions that did not require revision.

Formula:

False-Positive Revision Rate = Unnecessary Revisions / Total Revisions

2.9 Generalization

Measure performance on previously unseen tasks.

Compare performance on development cases and held-out evaluation cases.

2.10 Computational Cost

Record:

* Execution time.
* Token consumption.
* Number of reasoning operations.
* Number of graph operations.
* Revision operations.
* Memory usage where available.
* API and infrastructure costs.

3. Evidence Quality Metrics

Evaluate whether the system correctly identifies:

* Evidence origin.
* Source reliability.
* Evidence relevance.
* Conflicting information.
* Missing evidence.
* Unsupported assumptions.

Evidence quality assessments must be compared against predefined evaluation labels.

4. Comparative Evaluation

Compare experimental conditions:

A. Baseline reasoning.

B. Explicit dependency tracking.

C. Evidence-aware revision.

D. Failure-pattern analysis.

For every metric, report:

* Baseline result.
* Experimental result.
* Absolute difference.
* Relative difference where meaningful.
* Sample size.
* Uncertainty.
* Computational cost.

5. Metric Interpretation

Higher values are generally desirable for:

* Accuracy.
* Detection rate.
* Diagnosis accuracy.
* Tracing precision and recall.
* Recovery accuracy.
* Generalization.

Lower values are generally desirable for:

* Unsupported conclusion rate.
* Regression rate.
* False-positive revision rate.
* Computational cost.

No single metric should determine overall success.

6. Overall Evaluation

A mechanism should be considered beneficial only when improvements are supported by reproducible evidence.

A gain in recovery accuracy must be considered alongside regression rate and computational cost.

A system that produces more revisions is not necessarily a better system.

7. Evaluation Safeguards

* Define metrics before confirmatory experiments.
* Preserve raw predictions and evaluation labels.
* Do not change denominators to improve reported scores.
* Report missing and invalid observations.
* Avoid comparing results obtained under incompatible conditions.
* Evaluate on held-out cases.
* Document metric limitations.

8. Future Extensions

Potential future metrics:

* Root-cause localization accuracy.
* Revision minimality.
* Evidence provenance accuracy.
* Contradiction resolution quality.
* Adaptation effectiveness.
* Adaptation stability.
* Long-term knowledge consistency.

These metrics should be introduced only when reliable evaluation procedures are available.

9. Status

Initial metric specification.

Formal evaluation scripts and benchmark-specific scoring rules will be developed during implementation of EXP-001.
