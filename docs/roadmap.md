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
14. Added prediction-contract tests for every governed model artifact.
15. Added regression tests for manufacturing and clustering transformations.
16. Moved feature engineering and clustering implementations into `src.features`.
17. Moved model training implementations into `src.models`.
18. Extracted the Streamlit sidebar navigation controller into `app`.
19. Standardized page metadata and headings with shared Streamlit UI primitives.
20. Added an executable Streamlit release smoke test and verification guide.
21. Separated interactive model training from explicit artifact persistence.
22. Centralized optional Gemini tree analysis behind a tested service layer.
23. Extracted shared decision-tree serialization and Excel export helpers.
24. Split the seven navigation workflows into dedicated page controllers.
25. Isolated Streamlit session-state keys across decision-tree workflows.

## Remaining Work

- Refresh saved `.joblib` model artifacts with the active locked scikit-learn version after prediction changes are reviewed and accepted.
- Create the Streamlit Cloud app from `app/streamlit_app.py` and add the optional AI secret in the hosted app settings.

Each phase should stay small enough to review, run the verification suite, and commit independently.
