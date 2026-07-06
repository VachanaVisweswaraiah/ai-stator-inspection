import importlib
import subprocess
import sys


def test_core_modules_import_cleanly():
    modules = [
        "data_model",
        "k_means",
        "clustering.k_means",
        "create_fake_data",
    ]

    for module_name in modules:
        importlib.import_module(module_name)


def test_model_and_data_modules_import_without_runtime_side_effects():
    modules = [
        "Compute_fit",
        "create_fake_data",
        "steel_faults_PDT",
    ]

    for module_name in modules:
        result = subprocess.run(
            [sys.executable, "-c", f"import {module_name}"],
            check=False,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr
        assert result.stdout == ""
