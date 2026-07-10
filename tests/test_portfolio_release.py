from src.config.paths import PROJECT_ROOT


def test_portfolio_release_checklist_documents_public_release():
    checklist = (PROJECT_ROOT / "docs" / "portfolio_release.md").read_text()

    expected_fragments = [
        "https://github.com/VachanaVisweswaraiah/ai-stator-inspection",
        "https://ai-stator-inspection.streamlit.app/",
        "app/streamlit_app.py",
        "UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest",
        "git diff --check",
        "data/",
        "artifacts/models/",
        "artifacts/images/",
        "Optional AI analysis must fail gracefully",
    ]

    for fragment in expected_fragments:
        assert fragment in checklist


def test_release_docs_are_linked_from_readme_and_roadmap():
    readme = (PROJECT_ROOT / "README.md").read_text()
    roadmap = (PROJECT_ROOT / "docs" / "roadmap.md").read_text()

    assert "docs/portfolio_release.md" in readme
    assert "28. Added final portfolio release checklist" in roadmap
