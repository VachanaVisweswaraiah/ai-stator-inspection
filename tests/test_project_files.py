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
        "data/fake_data.xlsx",
        "data/Engineering_data.xlsx",
        "data/engineered_data_for_cluster.xlsx",
        "data/predicted_data.xlsx",
        "data/PDT_predicted_data.xlsx",
        "data/Iris.csv",
        "data/steel_faults_with_labels.csv",
        "data/Analysis_Data_augmented_csv.csv",
        "artifacts/models/decision_tree_model.joblib",
        "artifacts/models/probabilistic_decision_tree_model.joblib",
        "artifacts/models/probabilistic_decision_tree_model_Iris.joblib",
        "artifacts/models/probabilistic_decision_tree_model_Steel_Faults.joblib",
        "artifacts/images/decision_tree.png",
        "artifacts/images/decision_tree_graphviz.png",
    ]

    for relative_path in expected_files:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"


def test_runtime_assets_are_not_stored_at_repository_root():
    root_asset_patterns = ["*.csv", "*.xlsx", "*.joblib", "*.png"]
    root_assets = [
        asset.name
        for pattern in root_asset_patterns
        for asset in PROJECT_ROOT.glob(pattern)
    ]

    assert root_assets == []


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
