from Compute_fit import compute_fit as root_compute_fit
from Compute_fit import count_yes_no as root_count_yes_no
from create_fake_data import create_fake_dataset as root_create_fake_dataset
from data_model import data_model as root_data_model
from clustering.k_means import perform_kmeans as root_perform_kmeans

from src.config.paths import PROJECT_ROOT
from src.features import clustering, engineering


def test_engineering_facade_re_exports_existing_helpers():
    assert engineering.compute_fit is root_compute_fit
    assert engineering.count_yes_no is root_count_yes_no
    assert engineering.create_fake_dataset is root_create_fake_dataset
    assert engineering.data_model is root_data_model


def test_clustering_facade_re_exports_existing_helper():
    assert clustering.perform_kmeans is root_perform_kmeans


def test_streamlit_modules_import_feature_helpers_from_package_facades():
    app_modules = [
        "main.py",
        "app.py",
        "kmeans_main.py",
        "iris_viz.py",
        "steel_faults_viz.py",
        "vw_sample_data_viz.py",
    ]
    legacy_imports = [
        "from Compute_fit import",
        "from create_fake_data import",
        "from data_model import",
        "from clustering.k_means import",
        "from k_means import",
    ]

    for module_path in app_modules:
        source = (PROJECT_ROOT / module_path).read_text()

        assert "from src.features." in source
        for legacy_import in legacy_imports:
            assert legacy_import not in source
