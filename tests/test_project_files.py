from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_primary_application_files_exist():
    expected_files = [
        "main.py",
        "app.py",
        "requirements.txt",
        "pyproject.toml",
        "packages.txt",
    ]

    for relative_path in expected_files:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"


def test_runtime_datasets_and_model_artifacts_exist():
    expected_files = [
        "fake_data.xlsx",
        "Engineering_data.xlsx",
        "Iris.csv",
        "steel_faults_with_labels.csv",
        "Analysis_Data_augmented_csv.csv",
        "decision_tree_model.joblib",
        "probabilistic_decision_tree_model.joblib",
        "probabilistic_decision_tree_model_Iris.joblib",
        "probabilistic_decision_tree_model_Steel_Faults.joblib",
    ]

    for relative_path in expected_files:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"


def test_local_streamlit_flow_component_is_available():
    expected_paths = [
        "streamlit_flow/__init__.py",
        "streamlit_flow/elements.py",
        "streamlit_flow/layouts.py",
        "streamlit_flow/state.py",
        "streamlit_flow/frontend/build/index.html",
    ]

    for relative_path in expected_paths:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"
