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
9. Documented model artifact governance and refresh criteria.
10. Prepared Streamlit Cloud deployment settings and documentation.
11. Introduced model workflow facades under `src.models`.
12. Introduced feature and clustering facades under `src.features`.
13. Updated Streamlit visualization modules to use the feature facades consistently.

## Remaining Work

- Refresh saved `.joblib` model artifacts with the active locked scikit-learn version after prediction changes are reviewed and accepted.
- Move model training implementations into `src/models/` behind the existing workflow facade.
- Move feature engineering and clustering implementations into `src/features/` behind the existing facades.
- Split the large Streamlit app into smaller page/controller modules.
- Add focused tests for modeling outputs and key Streamlit data transformations.
- Improve UI consistency after the internal structure is stable.
- Create the Streamlit Cloud app from `app/streamlit_app.py` and add the optional AI secret in the hosted app settings.

Each phase should stay small enough to review, run the verification suite, and commit independently.
