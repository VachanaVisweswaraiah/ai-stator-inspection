from dataclasses import dataclass
from pathlib import Path

from src.config.paths import (
    DECISION_TREE_MODEL_PATH,
    IRIS_PROBABILISTIC_MODEL_PATH,
    PROBABILISTIC_DECISION_TREE_MODEL_PATH,
    STEEL_FAULTS_PROBABILISTIC_MODEL_PATH,
)


@dataclass(frozen=True)
class ModelArtifact:
    name: str
    path: Path
    training_module: str
    training_function: str
    depth: int
    prediction_context: str


MODEL_ARTIFACTS = (
    ModelArtifact(
        name="decision_tree_model.joblib",
        path=DECISION_TREE_MODEL_PATH,
        training_module="src.models.decision_tree",
        training_function="Decision_Tress",
        depth=6,
        prediction_context="Synthetic manufacturing decision tree predictions",
    ),
    ModelArtifact(
        name="probabilistic_decision_tree_model.joblib",
        path=PROBABILISTIC_DECISION_TREE_MODEL_PATH,
        training_module="src.models.probabilistic_tree",
        training_function="Probabilistic_Decision_Tree",
        depth=6,
        prediction_context="Synthetic manufacturing probabilistic decision tree predictions",
    ),
    ModelArtifact(
        name="probabilistic_decision_tree_model_Iris.joblib",
        path=IRIS_PROBABILISTIC_MODEL_PATH,
        training_module="src.models.iris_tree",
        training_function="Probabilistic_Decision_Tree_Iris",
        depth=4,
        prediction_context="Iris probabilistic decision tree predictions",
    ),
    ModelArtifact(
        name="probabilistic_decision_tree_model_Steel_Faults.joblib",
        path=STEEL_FAULTS_PROBABILISTIC_MODEL_PATH,
        training_module="src.models.steel_faults_tree",
        training_function="Probabilistic_Decision_Tree_Steel_Faults",
        depth=20,
        prediction_context="Steel faults probabilistic decision tree predictions",
    ),
)
