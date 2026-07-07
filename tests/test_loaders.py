from src.data import loaders
from src.models import artifacts


def test_core_dataset_loaders_return_dataframes():
    datasets = [
        loaders.load_fake_data(),
        loaders.load_engineering_data(),
        loaders.load_predicted_data(),
        loaders.load_pdt_predicted_data(),
        loaders.load_iris_data(),
        loaders.load_steel_faults_data(),
    ]

    for dataset in datasets:
        assert not dataset.empty


def test_vw_sample_loader_uses_expected_separator_format():
    dataset = loaders.load_vw_sample_data()

    assert not dataset.empty
    assert "Ergebnis" in dataset.columns


def test_existing_model_artifact_loaders_return_predictors():
    models = [
        artifacts.load_decision_tree_model(),
        artifacts.load_probabilistic_decision_tree_model(),
        artifacts.load_iris_probabilistic_model(),
        artifacts.load_steel_faults_probabilistic_model(),
    ]

    for model in models:
        assert hasattr(model, "predict")
