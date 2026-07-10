import tomllib

from src.config.paths import PROJECT_ROOT


def test_runtime_dependencies_are_pinned():
    pyproject = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text())
    dependencies = pyproject["project"]["dependencies"]
    critical_packages = [
        "joblib",
        "numpy",
        "pandas",
        "scikit-learn",
        "streamlit",
        "streamlit-cropper",
    ]

    for package_name in critical_packages:
        matching_dependencies = [
            dependency
            for dependency in dependencies
            if dependency.lower().startswith(f"{package_name.lower()}==")
        ]
        assert matching_dependencies, f"{package_name} must be pinned in pyproject.toml"


def test_reproducibility_guide_documents_core_commands():
    guide = (PROJECT_ROOT / "docs" / "reproducibility.md").read_text()

    expected_commands = [
        "uv sync",
        "uv run streamlit run app/streamlit_app.py",
        "UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest",
        "python3 -m compileall -q *.py app src clustering streamlit_flow tests ML_Dash_files",
        "git diff --check",
    ]

    for command in expected_commands:
        assert command in guide


def test_readme_links_reproducibility_guide():
    readme = (PROJECT_ROOT / "README.md").read_text()

    assert "docs/reproducibility.md" in readme
    assert "docs/portfolio_release.md" in readme
