# Model Artifacts

The application uses committed `.joblib` files so prediction workflows can run without retraining models at startup.

## Registry

| Artifact | Training Function | Depth | Runtime Use |
| --- | --- | ---: | --- |
| `decision_tree_model.joblib` | `src.models.decision_tree.Decision_Tress` | 6 | Synthetic manufacturing decision tree predictions |
| `probabilistic_decision_tree_model.joblib` | `src.models.probabilistic_tree.Probabilistic_Decision_Tree` | 6 | Synthetic manufacturing probabilistic decision tree predictions |
| `probabilistic_decision_tree_model_Iris.joblib` | `src.models.iris_tree.Probabilistic_Decision_Tree_Iris` | 4 | Iris probabilistic decision tree predictions |
| `probabilistic_decision_tree_model_Steel_Faults.joblib` | `src.models.steel_faults_tree.Probabilistic_Decision_Tree_Steel_Faults` | 20 | Steel faults probabilistic decision tree predictions |
| `probabilistic_decision_tree_model_VW_Sample.joblib` | `src.models.vw_sample_tree.Probabilistic_Decision_Tree_VW_Sample` | 5 | Optional offline Volkswagen sample artifact |

The same metadata is represented in `src/models/registry.py` so tests can validate that committed artifacts and documentation stay aligned. The Volkswagen artifact is governed but is not currently committed.

Interactive workflows train their selected-depth model in memory and do not write repository artifacts. Passing `persist=True` to a training workflow is reserved for an intentional offline artifact refresh.

## Refresh Policy

Model artifacts should only be refreshed when the refreshed models are intentionally accepted. A refresh must include:

- The training function and depth used for each artifact.
- A before-and-after prediction comparison on representative project datasets.
- Updated tests if expected predictions or model metrics intentionally change.
- A note in the commit message explaining that model artifacts were refreshed.

An attempted refresh with the current training code changed synthetic decision tree predictions, so the existing artifacts were kept. This protects current app behavior while making the remaining model-refresh work explicit.

## Known Compatibility Note

The current committed artifacts load successfully in the locked runtime, but scikit-learn may warn that some artifacts were serialized with `scikit-learn 1.4.1.post1` and are being loaded by the current runtime version. This is tracked as technical debt until the project intentionally refreshes and accepts updated model artifacts.
