Meta-Graph Research

Project Operating Manual

Version: 0.1
Status: Active research design
Project owner: Julianotion
Project type: Independent research
Primary language: English

⸻

1. Mission

Investigate whether explicit reasoning dependencies, evidence-aware revision, and structured failure analysis can improve the reliability of neuro-symbolic reasoning systems.

The long-term objective is to develop a dynamic meta-graph connecting:

• Claims
• Evidence
• Sources
• Assumptions
• Inference rules
• Contradictions
• Reasoning dependencies
• Model limitations
• Revision history
• Recurring failure patterns
• Proposed architectural changes

The system should be able to examine not only its conclusions but also the structure and limitations of the knowledge supporting them.

2. Research Question

Can explicit reasoning dependencies and evidence-aware self-revision improve a system’s ability to detect, diagnose, and recover from reasoning failures?

3. Core Hypothesis

Explicit representation of assumptions, evidence, contradictions, and reasoning dependencies may improve reasoning reliability.

Analysis of recurring failures may help identify structural weaknesses and generate testable architectural improvements.

This hypothesis is unverified.

4. Research Principles

• Mathematical validity does not guarantee empirical validity.
• Evidence must be distinguished from assumptions.
• Missing evidence is not evidence of falsity.
• Contradiction does not automatically establish which claim is false.
• Every important revision must preserve its history.
• Proposed improvements must be tested.
• Negative results must be documented.
• Uncertainty must be represented explicitly.
• Changes must be reversible whenever technically possible.
• No scientific claim should exceed the available evidence.

5. Research Architecture

Investigate three interconnected levels.

L1 — Claim Revision

Detect conclusions that are no longer supported by available evidence.

L2 — Dependency Revision

Identify assumptions and dependent conclusions affected by a change in evidence.

L3 — Structural Adaptation

Identify recurring failure patterns and propose modifications to the reasoning architecture.

Structural modifications must be evaluated independently before adoption.

6. Initial Experiment: EXP-001

Title:

Evidence-Aware Revision and Reasoning Dependency Tracking

Objective:

Compare reasoning systems with different levels of explicit knowledge representation and revision capabilities.

Experimental conditions:

A. Baseline reasoning.

B. Explicit dependency tracking.

C. Evidence-aware revision.

D. Failure-pattern analysis and proposed adaptation.

Introduce each mechanism separately.

Do not combine all mechanisms before measuring their individual contributions.

7. Failure Scenarios

The initial benchmark should include:

• Missing evidence.
• Contradictory evidence.
• False assumptions.
• New evidence invalidating earlier conclusions.
• Multiple conclusions depending on one assumption.
• Revisions causing unintended regressions.
• Misleading sources.
• Recurring reasoning failures.
• Incorrect diagnosis of failure causes.
• Ineffective architectural changes.
• Changes that improve familiar cases but damage unseen cases.
• Cases where uncertainty is the correct outcome.

Each case must have a documented expected result.

8. Evaluation Metrics

Measure:

• Answer accuracy.
• Failure detection rate.
• Unsupported conclusion rate.
• Assumption diagnosis accuracy.
• Dependency tracing accuracy.
• Recovery accuracy.
• Regression rate.
• Performance on unseen cases.
• False-positive revision rate.
• Computational cost.
• Revision cost.

Metric definitions must be specified before evaluation.

9. Research Workflow

For every experiment:

• Define the research question.
• Review related work.
• Specify the hypothesis.
• Define the baseline.
• Create controlled test cases.
• Define evaluation metrics.
• Implement the smallest reproducible version.
• Run baseline tests.
• Introduce one additional mechanism.
• Compare results.
• Analyze failures.
• Propose improvements.
• Test improvements on held-out cases.
• Document limitations.
• Publish the experiment report.

10. Related Work

Prioritize research and implementations from:

• IBM Logical Neural Networks.
• Neuro-symbolic AI.
• Belief revision.
• Truth maintenance systems.
• Non-monotonic reasoning.
• Knowledge provenance.
• Knowledge graphs.
• Automated failure diagnosis.
• Self-adaptive systems.
• AI self-refinement.

Reference repository:

https://github.com/IBM/LNN

IBM Research is a research reference, not a project affiliation.

Do not claim novelty before conducting a relevant literature review.

11. Autonomous Research Agent

The research agent should operate asynchronously within the approved project scope.

At every scheduled run, it should:

• Read this manual.
• Read the research agenda.
• Inspect open GitHub issues.
• Inspect recent experiment results.
• Identify the highest-priority unblocked task.
• Execute a bounded task.
• Run relevant tests.
• Record results.
• Create or update a GitHub issue or pull request.
• Update the progress log.
• Identify the next task.

The agent should not require the project owner to select every routine task.

12. Agent Permissions

The agent may:

• Research public scientific literature.
• Draft experiment specifications.
• Create GitHub issues.
• Implement isolated experimental code.
• Run authorized tests.
• Analyze experimental results.
• Propose architectural changes.
• Create branches.
• Open pull requests.
• Update documentation.
• Maintain the project progress log.

The agent must not:

• Merge its own unreviewed architectural changes.
• Delete historical experimental results.
• Change evaluation criteria silently.
• Invent citations or experimental results.
• Publish unverified scientific claims.
• Contact external researchers without authorization.
• Expose credentials or private information.
• Exceed configured execution or spending limits.

13. Revision Protocol

Every proposed change must document:

• Change ID.
• Previous state.
• Proposed state.
• Reason.
• Supporting evidence.
• Affected dependencies.
• Predicted benefits.
• Potential risks.
• Required tests.
• Observed results.
• Regression results.
• Final decision.

Possible decisions:

• ACCEPTED
• REJECTED
• DEFERRED

Preserve previous versions and their justifications.

14. Reproducibility

Every experiment must record:

• Experiment ID.
• Source-code commit.
• Dataset version.
• Configuration.
• Random seed, where applicable.
• Software dependencies.
• Execution environment.
• Raw outputs.
• Evaluation procedure.
• Limitations.

Never report a result that cannot be traced to an actual execution.

15. GitHub Workflow

Use GitHub Issues as the research task queue.

Use branches for experimental changes.

Use Pull Requests for substantive modifications.

Require automated tests before merging.

Protect the main branch.

Keep experiment specifications, results, and documentation version-controlled.

16. Attribution

The project owner defines the research direction, conceptual priorities, and research questions.

ChatGPT and other AI tools may assist with brainstorming, literature discovery, implementation, documentation, and analysis.

AI assistance must be disclosed.

AI-generated suggestions must be independently evaluated.

External research, code, and datasets must be attributed appropriately.

17. First Milestone

The first milestone is complete when:

• A reproducible benchmark exists.
• A baseline implementation runs.
• At least one enhanced configuration runs.
• Both configurations use the same evaluation procedure.
• Results include failures and regressions.
• A reproducible experiment report is available.
• Another researcher can reproduce the experiment.

A negative result is a valid research result.

⸻

End of document.
