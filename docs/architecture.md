# Architecture

PMV4 Analytics is organized around a Streamlit application layer and a gradually modularized Python package.

## Current Runtime Entry Points

- `app/streamlit_app.py` is the preferred Streamlit entry point for deployment.
- `main.py` remains available for backward-compatible local execution while functionality is migrated into `src/`.

## Target Module Boundaries

- `src/config/` contains shared project paths and will hold future configuration.
- `src/data/` contains dataset loading utilities and will hold future validation.
- `src/features/` will contain feature engineering and preprocessing logic.
- `src/models/` contains model artifact loading utilities, workflow facades, and will contain decision tree, probabilistic tree, and clustering implementations.
- `src/visualization/` will contain Plotly and tree visualization helpers.
- `src/services/` will contain external service integrations, including AI-assisted analysis.

The migration is intentionally incremental so that each refactor can be tested without changing user-facing functionality.

## Path Handling

Project files are resolved through `src/config/paths.py` instead of relying on the current working directory. This keeps scripts and the Streamlit deployment entry point aligned while preserving the existing data files and model artifacts in their current locations.

Runtime modules should use `src.data.loaders` for repository-owned datasets and `src.models.artifacts` for saved model artifacts. User-uploaded files remain handled directly by Streamlit because those paths are supplied at runtime.

Streamlit modules should import training/evaluation workflows through `src.models.workflows`. The facade currently preserves compatibility with the existing root-level training modules while giving the application a stable package boundary for future migration.
