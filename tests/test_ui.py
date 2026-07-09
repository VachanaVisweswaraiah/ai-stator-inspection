from app import ui
from src.config.paths import PROJECT_ROOT


def test_page_configuration_uses_project_brand(monkeypatch):
    captured = {}
    monkeypatch.setattr(
        ui.st,
        "set_page_config",
        lambda **kwargs: captured.update(kwargs),
    )

    ui.configure_page()

    assert captured == {
        "page_title": "PMV4 Analytics",
        "layout": "wide",
    }


def test_page_title_uses_native_streamlit_heading(monkeypatch):
    captured = []
    monkeypatch.setattr(ui.st, "title", captured.append)

    ui.render_page_title("IRIS Dataset Analysis")

    assert captured == ["IRIS Dataset Analysis"]


def test_primary_app_uses_shared_ui_primitives():
    source = (PROJECT_ROOT / "main.py").read_text()

    assert "configure_page()" in source
    assert source.count("render_page_title(") == 7
    assert 'style="text-align: center;"' not in source
