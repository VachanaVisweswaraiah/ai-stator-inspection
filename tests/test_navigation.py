from app import navigation
from src.config.paths import PROJECT_ROOT


class SidebarContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False


def test_navigation_preserves_existing_labels_and_order():
    assert list(navigation.SECTIONS.items()) == [
        ("Data Understanding", "Data Understanding"),
        ("K-Means", "k-means"),
        ("Decision Tree", "Decision Tree"),
        ("Probabilistic Decision Tree", "Probabilistic Decision Tree"),
        ("Iris PDT", "Iris PDT"),
        ("Steel Faults PDT", "Steel Faults PDT"),
        ("Volkswagen PDT", "Volkswagen PDT"),
    ]


def test_navigation_returns_selected_internal_section(monkeypatch):
    captured = {}

    def fake_option_menu(title, options, default_index):
        captured.update(
            title=title,
            options=options,
            default_index=default_index,
        )
        return "K-Means"

    monkeypatch.setattr(navigation.st, "sidebar", SidebarContext())
    monkeypatch.setattr(navigation, "option_menu", fake_option_menu)

    assert navigation.select_section() == "k-means"
    assert captured == {
        "title": "PMV4 Analytics",
        "options": list(navigation.SECTIONS),
        "default_index": 0,
    }


def test_main_delegates_sidebar_navigation_to_controller():
    source = (PROJECT_ROOT / "main.py").read_text()

    assert "from app.navigation import select_section" in source
    assert "selected_section = select_section()" in source
    assert "from streamlit_option_menu import option_menu" not in source
