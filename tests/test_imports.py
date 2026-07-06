import importlib


def test_core_modules_import_cleanly():
    modules = [
        "data_model",
        "k_means",
        "clustering.k_means",
        "create_fake_data",
    ]

    for module_name in modules:
        importlib.import_module(module_name)
