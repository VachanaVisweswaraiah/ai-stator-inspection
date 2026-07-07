from src.config.paths import PROJECT_ROOT


def test_github_actions_quality_workflow_exists():
    workflow_path = PROJECT_ROOT / ".github" / "workflows" / "ci.yml"
    workflow = workflow_path.read_text()

    expected_fragments = [
        "name: CI",
        "actions/checkout@v4",
        "actions/setup-python@v5",
        "astral-sh/setup-uv@v5",
        "uv lock --check",
        "uv sync --locked",
        "UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest",
        "uv run python -m compileall -q *.py app src clustering streamlit_flow tests ML_Dash_files",
    ]

    for fragment in expected_fragments:
        assert fragment in workflow


def test_project_docs_reference_ci_and_roadmap():
    readme = (PROJECT_ROOT / "README.md").read_text()
    reproducibility = (PROJECT_ROOT / "docs" / "reproducibility.md").read_text()
    roadmap = PROJECT_ROOT / "docs" / "roadmap.md"

    assert ".github/workflows/ci.yml" in readme
    assert "docs/roadmap.md" in readme
    assert "GitHub Actions" in reproducibility
    assert roadmap.is_file()
