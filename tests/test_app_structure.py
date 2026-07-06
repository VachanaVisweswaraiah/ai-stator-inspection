from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_portfolio_project_structure_exists():
    expected_paths = [
        "app/__init__.py",
        "app/streamlit_app.py",
        "src/__init__.py",
        "src/config/__init__.py",
        "src/data/__init__.py",
        "src/features/__init__.py",
        "src/models/__init__.py",
        "src/services/__init__.py",
        "src/visualization/__init__.py",
        "docs/architecture.md",
    ]

    for relative_path in expected_paths:
        assert (PROJECT_ROOT / relative_path).is_file(), f"Missing {relative_path}"
