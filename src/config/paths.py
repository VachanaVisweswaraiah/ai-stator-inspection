from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def project_path(*parts: str) -> Path:
    return PROJECT_ROOT.joinpath(*parts)


FAKE_DATA_PATH = project_path("fake_data.xlsx")
ENGINEERING_DATA_PATH = project_path("Engineering_data.xlsx")
ENGINEERED_CLUSTER_DATA_PATH = project_path("engineered_data_for_cluster.xlsx")
PREDICTED_DATA_PATH = project_path("predicted_data.xlsx")
PDT_PREDICTED_DATA_PATH = project_path("PDT_predicted_data.xlsx")
IRIS_DATA_PATH = project_path("Iris.csv")
STEEL_FAULTS_DATA_PATH = project_path("steel_faults_with_labels.csv")
VW_SAMPLE_DATA_PATH = project_path("Analysis_Data_augmented_csv.csv")

DECISION_TREE_MODEL_PATH = project_path("decision_tree_model.joblib")
PROBABILISTIC_DECISION_TREE_MODEL_PATH = project_path("probabilistic_decision_tree_model.joblib")
IRIS_PROBABILISTIC_MODEL_PATH = project_path("probabilistic_decision_tree_model_Iris.joblib")
STEEL_FAULTS_PROBABILISTIC_MODEL_PATH = project_path("probabilistic_decision_tree_model_Steel_Faults.joblib")
VW_SAMPLE_PROBABILISTIC_MODEL_PATH = project_path("probabilistic_decision_tree_model_VW_Sample.joblib")
