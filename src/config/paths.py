from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def project_path(*parts: str) -> Path:
    return PROJECT_ROOT.joinpath(*parts)


DATA_DIR = project_path("data")
MODEL_ARTIFACTS_DIR = project_path("artifacts", "models")
IMAGE_ARTIFACTS_DIR = project_path("artifacts", "images")

FAKE_DATA_PATH = DATA_DIR / "fake_data.xlsx"
ENGINEERING_DATA_PATH = DATA_DIR / "Engineering_data.xlsx"
ENGINEERED_CLUSTER_DATA_PATH = DATA_DIR / "engineered_data_for_cluster.xlsx"
PREDICTED_DATA_PATH = DATA_DIR / "predicted_data.xlsx"
PDT_PREDICTED_DATA_PATH = DATA_DIR / "PDT_predicted_data.xlsx"
IRIS_DATA_PATH = DATA_DIR / "Iris.csv"
STEEL_FAULTS_DATA_PATH = DATA_DIR / "steel_faults_with_labels.csv"
VW_SAMPLE_DATA_PATH = DATA_DIR / "Analysis_Data_augmented_csv.csv"

DECISION_TREE_MODEL_PATH = MODEL_ARTIFACTS_DIR / "decision_tree_model.joblib"
PROBABILISTIC_DECISION_TREE_MODEL_PATH = MODEL_ARTIFACTS_DIR / "probabilistic_decision_tree_model.joblib"
IRIS_PROBABILISTIC_MODEL_PATH = MODEL_ARTIFACTS_DIR / "probabilistic_decision_tree_model_Iris.joblib"
STEEL_FAULTS_PROBABILISTIC_MODEL_PATH = MODEL_ARTIFACTS_DIR / "probabilistic_decision_tree_model_Steel_Faults.joblib"
VW_SAMPLE_PROBABILISTIC_MODEL_PATH = MODEL_ARTIFACTS_DIR / "probabilistic_decision_tree_model_VW_Sample.joblib"
