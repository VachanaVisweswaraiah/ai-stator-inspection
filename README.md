# PMV4 Analytics

PMV4 Analytics is a Streamlit-based machine learning dashboard for exploring manufacturing-style process data and benchmark classification datasets. The app combines data understanding, clustering, decision tree modeling, probabilistic decision tree views, and optional AI-assisted analysis of tree structures.

The project is being developed as a portfolio-grade ML application with reproducible setup, automated baseline checks, structured model workflows, and deployment-ready documentation.

## Current App Entry Point

The primary Streamlit app is:

```bash
streamlit run main.py
```

`main.py` is the most complete app and includes these navigation sections:

- Data Understanding
- K-Means
- Decision Tree
- Probabilistic Decision Tree
- Iris PDT
- Steel Faults PDT
- Volkswagen PDT

There is also an older/smaller Streamlit app in `app.py`, plus a Dash prototype in `ML_Dash_files/main.py`.

## Project Contents

- `main.py` - primary Streamlit dashboard.
- `app.py` - smaller legacy Streamlit dashboard.
- `*_PDT.py` - probabilistic decision tree model helpers for each dataset.
- `*_viz.py` - Streamlit visualization flows for dataset-specific probabilistic decision trees.
- `k_means.py` and `clustering/k_means.py` - K-Means helper functions.
- `data_model.py` - engineering target/range definitions for synthetic data.
- `*.csv` and `*.xlsx` files - current runtime datasets and generated prediction tables.
- `*.joblib` files - current trained model artifacts used by the app.
- `streamlit_flow/` - local Streamlit flow component code and frontend build.

## Dependencies

This project now supports a `uv` workflow for local development while keeping `requirements.txt` for Streamlit-friendly deployment.

Recommended local setup:

```bash
uv sync
uv run streamlit run main.py
```

Fallback setup:

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run main.py
```

System package note: `packages.txt` currently declares `graphviz`, which is needed by Graphviz-related tree visualization workflows in deployed environments.

## Secrets

The AI analysis feature expects a Streamlit secret named:

```toml
[api_keys]
gemini = "your-api-key"
```

For local development, place this in `.streamlit/secrets.toml`. That file is intentionally ignored by Git.

## Quality Checks

Run the baseline verification suite before changing model, data, or Streamlit workflow code:

```bash
python3 -m compileall -q *.py clustering streamlit_flow tests ML_Dash_files
UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest
```

Manual Streamlit verification:

```bash
streamlit run main.py
```

Current engineering observations:

- `main.py` is the real full app entry point.
- `app.py` imports successfully and appears to be a smaller legacy version.
- `main.py` imports successfully once declared dependencies are installed.
- Importing `main.py` currently triggers model/data work from imported modules, including steel-fault model training output.
- Matplotlib may warn about cache directories when the home cache path is not writable.
- A real Streamlit browser session is still the best way to verify every tab and interaction.

## Development Roadmap

The application will evolve in focused phases to keep functionality stable while improving engineering quality:

1. Establish automated baseline verification.
2. Organize datasets, models, generated outputs, and project assets.
3. Modularize the app without changing behavior.
4. Add tests for data processing, modeling helpers, and smoke imports.
5. Polish the UI and project presentation.
6. Deploy the Streamlit app from the cleaned GitHub repository.
