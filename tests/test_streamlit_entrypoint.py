from streamlit.testing.v1 import AppTest

from src.config.paths import PROJECT_ROOT


def test_deployment_entrypoint_runs_without_exceptions():
    app = AppTest.from_file(
        str(PROJECT_ROOT / "app" / "streamlit_app.py")
    )

    app.run(timeout=60)

    assert not app.exception
    assert [title.value for title in app.title] == [
        "Box and Cylinder Analysis"
    ]
