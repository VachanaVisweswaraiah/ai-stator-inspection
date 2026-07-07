from src.config.paths import PROJECT_ROOT


def test_streamlit_config_is_committed_without_secrets():
    config = PROJECT_ROOT / ".streamlit" / "config.toml"
    gitignore = (PROJECT_ROOT / ".gitignore").read_text()

    assert config.is_file()
    assert ".streamlit/secrets.toml" in gitignore


def test_deployment_docs_define_streamlit_cloud_entry_point():
    deployment_doc = (PROJECT_ROOT / "docs" / "deployment.md").read_text()
    readme = (PROJECT_ROOT / "README.md").read_text()

    expected_fragments = [
        "VachanaVisweswaraiah/ai-stator-inspection",
        "Branch: `main`",
        "Main file path: `app/streamlit_app.py`",
        "Python version: `3.12`",
        "requirements.txt",
        "packages.txt",
        ".streamlit/config.toml",
    ]

    for fragment in expected_fragments:
        assert fragment in deployment_doc

    assert "docs/deployment.md" in readme
    assert "app/streamlit_app.py" in readme


def test_deployment_system_packages_include_graphviz():
    packages = (PROJECT_ROOT / "packages.txt").read_text().splitlines()

    assert "graphviz" in packages
