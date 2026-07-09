from Decision_Tress import Decision_Tress as root_decision_tree
from Iris_PDT import Probabilistic_Decision_Tree_Iris as root_iris_pdt
from Probabilistic_DT import Probabilistic_Decision_Tree as root_probabilistic_tree
from steel_faults_PDT import (
    Probabilistic_Decision_Tree_Steel_Faults as root_steel_faults_pdt,
)
from vw_sample_data_PDT import Probabilistic_Decision_Tree_VW_Sample as root_vw_sample_pdt

from src.config.paths import PROJECT_ROOT
from src.models import workflows


def test_legacy_model_modules_re_export_package_workflows():
    expected_exports = {
        "Decision_Tress": root_decision_tree,
        "Probabilistic_Decision_Tree": root_probabilistic_tree,
        "Probabilistic_Decision_Tree_Iris": root_iris_pdt,
        "Probabilistic_Decision_Tree_Steel_Faults": root_steel_faults_pdt,
        "Probabilistic_Decision_Tree_VW_Sample": root_vw_sample_pdt,
    }

    for export_name, root_function in expected_exports.items():
        assert getattr(workflows, export_name) is root_function
        assert export_name in workflows.__all__


def test_model_training_implementations_are_owned_by_package_modules():
    expected_modules = {
        "Decision_Tress": "src.models.decision_tree",
        "Probabilistic_Decision_Tree": "src.models.probabilistic_tree",
        "Probabilistic_Decision_Tree_Iris": "src.models.iris_tree",
        "Probabilistic_Decision_Tree_Steel_Faults": (
            "src.models.steel_faults_tree"
        ),
        "Probabilistic_Decision_Tree_VW_Sample": (
            "src.models.vw_sample_tree"
        ),
    }

    for function_name, module_name in expected_modules.items():
        assert getattr(workflows, function_name).__module__ == module_name


def test_streamlit_modules_import_model_workflows_from_package_facade():
    streamlit_modules = [
        "main.py",
        "iris_viz.py",
        "steel_faults_viz.py",
        "vw_sample_data_viz.py",
    ]
    legacy_imports = [
        "from Decision_Tress import",
        "from Probabilistic_DT import",
        "from Iris_PDT import",
        "from steel_faults_PDT import",
        "from vw_sample_data_PDT import",
    ]

    for module_path in streamlit_modules:
        source = (PROJECT_ROOT / module_path).read_text()

        assert "from src.models.workflows import" in source
        for legacy_import in legacy_imports:
            assert legacy_import not in source
