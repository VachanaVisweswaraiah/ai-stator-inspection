# Project Roadmap

This roadmap tracks the cleanup phases used to turn PMV4 Analytics into a portfolio-grade machine learning application while preserving existing functionality.

## Completed

1. Established a safety baseline with smoke tests and project documentation.
2. Removed import-time side effects from model and data generation modules.
3. Introduced the `app/` and `src/` package structure without moving the primary Streamlit workflow.
4. Centralized project file paths in `src.config.paths`.
5. Updated Streamlit-facing modules to use centralized project paths.
6. Added dataset and model artifact loader helpers.
7. Documented reproducible local setup and dependency expectations.
8. Added GitHub Actions CI for automated quality checks.

## Remaining Work

- Refresh saved `.joblib` model artifacts with the active locked scikit-learn version.
- Move model training workflows into `src/models/` behind stable interfaces.
- Move feature engineering logic into `src/features/`.
- Split the large Streamlit app into smaller page/controller modules.
- Add focused tests for modeling outputs and key Streamlit data transformations.
- Improve UI consistency after the internal structure is stable.
- Configure Streamlit deployment from `app/streamlit_app.py`.

Each phase should stay small enough to review, run the verification suite, and commit independently.
