import joblib

from src.config.paths import (
    DECISION_TREE_MODEL_PATH,
    IRIS_PROBABILISTIC_MODEL_PATH,
    PROBABILISTIC_DECISION_TREE_MODEL_PATH,
    STEEL_FAULTS_PROBABILISTIC_MODEL_PATH,
    VW_SAMPLE_PROBABILISTIC_MODEL_PATH,
)


def load_decision_tree_model():
    return joblib.load(DECISION_TREE_MODEL_PATH)


def load_probabilistic_decision_tree_model():
    return joblib.load(PROBABILISTIC_DECISION_TREE_MODEL_PATH)


def load_iris_probabilistic_model():
    return joblib.load(IRIS_PROBABILISTIC_MODEL_PATH)


def load_steel_faults_probabilistic_model():
    return joblib.load(STEEL_FAULTS_PROBABILISTIC_MODEL_PATH)


def load_vw_sample_probabilistic_model():
    return joblib.load(VW_SAMPLE_PROBABILISTIC_MODEL_PATH)
