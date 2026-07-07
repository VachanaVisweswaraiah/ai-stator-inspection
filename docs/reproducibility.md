# Reproducibility

This project uses a locked Python environment so the Streamlit application, tests, datasets, and model artifacts can be recreated consistently.

## Runtime

- Python: `3.12`
- Dependency manager: `uv`
- Primary app entry point: `app/streamlit_app.py`
- Deployment fallback: `requirements.txt`

The canonical dependency sources are:

- `pyproject.toml` for direct project dependencies.
- `uv.lock` for the fully resolved local development environment.
- `requirements.txt` for Streamlit Community Cloud style deployments.
- `packages.txt` for system packages required by deployment environments.

## Local Setup

Install the locked environment:

```bash
uv sync
```

Run the Streamlit app:

```bash
uv run streamlit run app/streamlit_app.py
```

Run the verification suite:

```bash
UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest
python3 -m compileall -q *.py app src clustering streamlit_flow tests ML_Dash_files
```

## Deployment Setup

Streamlit deployments can install from `requirements.txt` and use this launch command:

```bash
streamlit run app/streamlit_app.py
```

The Graphviz system package is declared in `packages.txt` for tree visualization workflows.

## Secrets

The optional AI analysis feature expects this Streamlit secret:

```toml
[api_keys]
gemini = "your-api-key"
```

Local secrets belong in `.streamlit/secrets.toml`, which is ignored by Git.

## Model Artifacts

The repository includes pre-trained `.joblib` model artifacts so the app can make predictions without retraining on startup.

Current verification loads these artifacts successfully with the locked runtime. During tests, scikit-learn may warn that some artifacts were serialized with `scikit-learn 1.4.1.post1` and are being loaded by the current runtime version. This is documented technical debt rather than a current app failure.

Future model-refresh work should retrain and reserialize all committed model artifacts with the active locked scikit-learn version, then update the verification suite against the refreshed artifacts.
