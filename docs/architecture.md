# Architecture

PMV4 Analytics is organized around a Streamlit application layer and a gradually modularized Python package.

## Current Runtime Entry Points

- `app/streamlit_app.py` is the preferred Streamlit entry point for deployment.
- `main.py` remains available for backward-compatible local execution while functionality is migrated into `src/`.

## Target Module Boundaries

- `src/config/` contains shared project paths and will hold future configuration.
- `src/data/` will contain dataset loading and validation utilities.
- `src/features/` will contain feature engineering and preprocessing logic.
- `src/models/` will contain decision tree, probabilistic tree, and clustering workflows.
- `src/visualization/` will contain Plotly and tree visualization helpers.
- `src/services/` will contain external service integrations, including AI-assisted analysis.

The migration is intentionally incremental so that each refactor can be tested without changing user-facing functionality.

## Path Handling

Project files are resolved through `src/config/paths.py` instead of relying on the current working directory. This keeps scripts and the Streamlit deployment entry point aligned while preserving the existing data files and model artifacts in their current locations.
