from pathlib import Path

import pandas as pd

from app.navigation import SECTIONS
from app.pages import decision_tree
from src.config.paths import PROJECT_ROOT


PAGE_MODULES = {
    "Data Understanding": "data_understanding.py",
    "k-means": "clustering.py",
    "Decision Tree": "decision_tree.py",
    "Probabilistic Decision Tree": "probabilistic_tree.py",
    "Iris PDT": "iris.py",
    "Steel Faults PDT": "steel_faults.py",
    "Volkswagen PDT": "volkswagen.py",
}


def test_every_navigation_section_has_a_page_controller():
    assert set(PAGE_MODULES) == set(SECTIONS.values())

    pages_directory = PROJECT_ROOT / "app" / "pages"
    for module_name in PAGE_MODULES.values():
        assert (pages_directory / module_name).is_file()


def test_page_controllers_do_not_import_main_module():
    for module_name in PAGE_MODULES.values():
        source = (
            PROJECT_ROOT / "app" / "pages" / module_name
        ).read_text()
        assert "from main import" not in source
        assert "import main" not in source


def test_main_delegates_page_composition_to_controllers():
    source = (PROJECT_ROOT / "main.py").read_text()

    assert "page_renderers = {" in source
    assert "page_renderers[selected_section]()" in source
    assert "elif selected_section" not in source


def test_decision_tree_controller_preserves_depth_workflow(
    monkeypatch,
):
    rendered_depths = []
    dataframe = pd.DataFrame({"Prediction": ["OK"]})

    monkeypatch.setattr(
        decision_tree,
        "render_page_title",
        lambda title: None,
    )
    monkeypatch.setattr(
        decision_tree.st,
        "header",
        lambda title: None,
    )
    monkeypatch.setattr(
        decision_tree.st,
        "dataframe",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(
        decision_tree.st,
        "slider",
        lambda *args, **kwargs: 3,
    )

    decision_tree.render(
        lambda: (dataframe.copy(), dataframe.copy()),
        rendered_depths.append,
    )

    assert rendered_depths == [3]
