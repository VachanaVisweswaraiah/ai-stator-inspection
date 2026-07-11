# PMV4 Analytics

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white)
![Graphviz](https://img.shields.io/badge/Graphviz-Visualization-2F7EBD)
![pytest](https://img.shields.io/badge/pytest-Tested-0A9EDC?logo=pytest&logoColor=white)

Developed in collaboration with Volkswagen Group, PMV4 Analytics is a deployed Streamlit machine learning dashboard for manufacturing-style process analysis and benchmark classification workflows. It combines data exploration, clustering, decision-tree prediction, probabilistic tree visualization, and optional AI-assisted tree interpretation in one application.

Live app: https://ai-stator-inspection.streamlit.app/

Repository: https://github.com/VachanaVisweswaraiah/ai-stator-inspection

Presentation materials: https://drive.google.com/drive/folders/1rEl3tcPdDUH7BGAQLuHMXQpM-KajDp8z?usp=sharing

## Project Highlights

- End-to-end Streamlit app deployed from a cleaned GitHub repository.
- Modularized `app/` and `src/` structure for UI controllers, data loading, feature engineering, model workflows, services, and visualization helpers.
- Runtime datasets organized under `data/` and governed model artifacts under `artifacts/models/`.
- Automated CI with lockfile validation, tests, Python compilation, and whitespace checks.
- Streamlit smoke tests covering every navigation workflow.
- Prediction-contract tests for committed model artifacts.
- Documented reproducibility, deployment, model artifact governance, and release verification.

## Application Workflows

The app includes seven primary workflows:

- Data Understanding: synthetic box-and-cylinder manufacturing data exploration.
- K-Means: clustering analysis and fitting-group visualization.
- Decision Tree: deterministic decision-tree predictions and tree inspection.
- Probabilistic Decision Tree: probabilistic tree workflow for synthetic manufacturing data.
- Iris PDT: probabilistic decision-tree workflow for the Iris dataset.
- Steel Faults PDT: probabilistic decision-tree workflow for steel fault classification.
- Volkswagen PDT: probabilistic decision-tree workflow based on Volkswagen Group sample data.

Optional AI analysis is available when a Gemini-compatible API key is configured in Streamlit secrets. Without the secret, the rest of the app remains available and the AI feature displays a graceful availability warning.

## Architecture

```text
app/
  streamlit_app.py        Deployment entry point
  navigation.py           Sidebar navigation contract
  pages/                  Page controllers for each workflow
  ai_analysis.py          Optional AI analysis UI
  ui.py                   Shared Streamlit UI primitives

src/
  config/                 Project paths and configuration
  data/                   Dataset loaders
  features/               Feature engineering and clustering logic
  models/                 Model workflows, artifact loading, registry
  services/               External service integrations
  visualization/          Shared tree/export helpers

data/                     Committed runtime datasets
artifacts/models/         Committed model artifacts
artifacts/images/         Reference tree images
docs/                     Architecture, deployment, release, reproducibility docs
tests/                    Unit, contract, CI, and Streamlit smoke tests
```

`app/streamlit_app.py` is the deployment entry point. `main.py` remains as the compatibility coordinator while the app continues its incremental migration into the structured package layout.

## Quick Start

This project uses `uv` for reproducible local development.

```bash
uv sync
uv run streamlit run app/streamlit_app.py
```

Fallback setup for environments that install from `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app/streamlit_app.py
```

System dependency note: `packages.txt` declares `graphviz` for Graphviz-backed tree visualization workflows in deployed environments.

## Quality Gate

Run the release gate before changing model, data, or Streamlit workflow behavior:

```bash
UV_CACHE_DIR=.uv-cache uv lock --check
UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest
UV_CACHE_DIR=.uv-cache uv run --python 3.12 python -m compileall -q *.py app src clustering streamlit_flow tests ML_Dash_files
git diff --check
```

The same baseline is enforced in `.github/workflows/ci.yml`.

## Deployment

Streamlit Community Cloud should use:

- Repository: `VachanaVisweswaraiah/ai-stator-inspection`
- Branch: `main`
- Main file path: `app/streamlit_app.py`
- Python version: `3.12`
- Python dependencies: `requirements.txt`
- System packages: `packages.txt`
- Streamlit config: `.streamlit/config.toml`

The deployed app is available at https://ai-stator-inspection.streamlit.app/.

## Optional Secrets

The AI analysis feature expects this Streamlit secret:

```toml
[api_keys]
gemini = "your-api-key"
```

For local development, place this in `.streamlit/secrets.toml`. That file is intentionally ignored by Git.

## Project Documentation

- `docs/architecture.md` - module boundaries and runtime structure.
- `docs/reproducibility.md` - dependency and verification contract.
- `docs/deployment.md` - Streamlit Cloud deployment settings.
- `docs/release_verification.md` - release and hosted-app verification steps.
- `docs/portfolio_release.md` - final portfolio presentation checklist.
- `docs/model_artifacts.md` - model artifact registry and refresh policy.
- `docs/roadmap.md` - completed cleanup phases and remaining technical debt.

## Current Technical Notes

- Saved `.joblib` model artifacts load successfully, but some were serialized with an older scikit-learn version and may emit compatibility warnings under the locked runtime.
- Model artifact refreshes should be handled as an intentional future phase because refreshed models may change predictions or metrics.
- Root-level compatibility modules remain while the app continues moving toward the structured `app/` and `src/` architecture.
