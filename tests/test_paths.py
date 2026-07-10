from pathlib import Path

from src.config import paths


def test_project_root_points_to_repository_root():
    assert paths.PROJECT_ROOT.is_absolute()
    assert (paths.PROJECT_ROOT / "README.md").is_file()
    assert (paths.PROJECT_ROOT / "app" / "streamlit_app.py").is_file()


def test_project_path_resolves_inside_repository():
    resolved_path = paths.project_path("data", "fake_data.xlsx")

    assert isinstance(resolved_path, Path)
    assert resolved_path == paths.FAKE_DATA_PATH
    assert resolved_path.is_file()


def test_asset_directories_are_named_explicitly():
    assert paths.DATA_DIR == paths.project_path("data")
    assert paths.MODEL_ARTIFACTS_DIR == paths.project_path("artifacts", "models")
    assert paths.IMAGE_ARTIFACTS_DIR == paths.project_path("artifacts", "images")
    assert paths.DATA_DIR.is_dir()
    assert paths.MODEL_ARTIFACTS_DIR.is_dir()
    assert paths.IMAGE_ARTIFACTS_DIR.is_dir()


def test_core_data_and_model_paths_are_absolute():
    core_paths = [
        paths.FAKE_DATA_PATH,
        paths.IRIS_DATA_PATH,
        paths.STEEL_FAULTS_DATA_PATH,
        paths.VW_SAMPLE_DATA_PATH,
        paths.DECISION_TREE_MODEL_PATH,
        paths.PROBABILISTIC_DECISION_TREE_MODEL_PATH,
        paths.IRIS_PROBABILISTIC_MODEL_PATH,
        paths.STEEL_FAULTS_PROBABILISTIC_MODEL_PATH,
    ]

    assert all(path.is_absolute() for path in core_paths)


def test_runtime_modules_use_centralized_project_paths():
    runtime_files = [
        "app.py",
        "main.py",
        "kmeans_main.py",
        "iris_viz.py",
        "steel_faults_viz.py",
        "vw_sample_data_viz.py",
    ]
    project_assets = [
        "data/fake_data.xlsx",
        "data/Engineering_data.xlsx",
        "data/engineered_data_for_cluster.xlsx",
        "data/predicted_data.xlsx",
        "data/PDT_predicted_data.xlsx",
        "data/Analysis_Data_augmented_csv.csv",
        "artifacts/models/decision_tree_model.joblib",
        "artifacts/models/probabilistic_decision_tree_model.joblib",
        "artifacts/models/probabilistic_decision_tree_model_Iris.joblib",
        "artifacts/models/probabilistic_decision_tree_model_Steel_Faults.joblib",
        "artifacts/models/probabilistic_decision_tree_model_VW_Sample.joblib",
    ]

    for runtime_file in runtime_files:
        source = paths.project_path(runtime_file).read_text()
        for asset_name in project_assets:
            assert asset_name not in source, f"{runtime_file} should use src.config.paths for {asset_name}"
