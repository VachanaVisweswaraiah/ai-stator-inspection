# Architecture

PMV4 Analytics is organized around a Streamlit application layer and a gradually modularized Python package.

## Current Runtime Entry Points

- `app/streamlit_app.py` is the preferred Streamlit entry point for deployment.
- `app/navigation.py` owns the sidebar navigation contract.
- `app/pages/` contains one controller for each navigable workflow.
- `app/ui.py` owns shared page configuration and heading primitives.
- `main.py` remains available for backward-compatible local execution and supplies existing visualization callbacks to the page controllers.

## Target Module Boundaries

- `src/config/` contains shared project paths and will hold future configuration.
- `src/data/` contains dataset loading utilities and will hold future validation.
- `src/features/` contains feature-engineering and clustering implementations.
- `src/models/` contains model training workflows and artifact loading utilities.
- `src/visualization/` contains reusable tree serialization and data-export helpers and will hold additional Plotly and Streamlit-independent visualization logic.
- `src/services/` will contain external service integrations, including AI-assisted analysis.
- `src/services/tree_analysis.py` owns Gemini-compatible decision-tree analysis without depending on Streamlit.

The migration is intentionally incremental so that each refactor can be tested without changing user-facing functionality.

Page controllers own dataset presentation, controls, and workflow composition. They do not import `main.py`; synthetic-data pages receive existing callbacks from the coordinator, while dataset-specific pages import their workflows locally to avoid circular dependencies.

## Path Handling

Project files are resolved through `src/config/paths.py` instead of relying on the current working directory. This keeps scripts and the Streamlit deployment entry point aligned while preserving the existing data files and model artifacts in their current locations.

Runtime modules should use `src.data.loaders` for repository-owned datasets and `src.models.artifacts` for saved model artifacts. User-uploaded files remain handled directly by Streamlit because those paths are supplied at runtime.

Streamlit modules import training and evaluation workflows through `src.models.workflows`. Root-level training modules remain as compatibility entry points.

Primary app modules import engineering and clustering helpers through `src.features`. Root-level feature modules remain as compatibility entry points.

Shared Streamlit rendering for optional AI analysis lives in `app/ai_analysis.py`. Missing hosted secrets are handled as a disabled optional capability instead of an application failure.

Decision-tree serialization and Excel download generation are shared through `src.visualization`, with dataset-specific preparation and class labels supplied by the calling workflow.

Interactive Streamlit state is namespaced by workflow. Decision-tree expert-insight forms use workflow-specific hypothesis lists, reset flags, form keys, and field keys so navigating between pages does not reuse stale form state from another workflow.
