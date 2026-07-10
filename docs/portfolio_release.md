# Portfolio Release Checklist

This checklist summarizes the release standard for PMV4 Analytics as a portfolio-ready machine learning project.

## Release Links

- GitHub repository: `https://github.com/VachanaVisweswaraiah/ai-stator-inspection`
- Streamlit app: `https://ai-stator-inspection.streamlit.app/`
- Deployment entry point: `app/streamlit_app.py`

## Release Gate

Run these commands before tagging, presenting, or materially changing the deployed app:

```bash
UV_CACHE_DIR=.uv-cache uv lock --check
UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest
UV_CACHE_DIR=.uv-cache uv run --python 3.12 python -m compileall -q *.py app src clustering streamlit_flow tests ML_Dash_files
git diff --check
```

The same gate is mirrored in `.github/workflows/ci.yml`.

## Review Standard

- The app must launch from `app/streamlit_app.py`.
- Every sidebar workflow must render without Streamlit exceptions.
- Committed datasets must live under `data/`.
- Committed model artifacts must live under `artifacts/models/`.
- Generated reference images must live under `artifacts/images/`.
- Runtime code should load project files through `src.config.paths`, `src.data.loaders`, and `src.models.artifacts`.
- Optional AI analysis must fail gracefully when the hosted secret is absent.
- Model artifact refreshes require explicit acceptance of prediction changes.

## Known Technical Debt

- The saved `.joblib` model artifacts load under the locked runtime, but some were serialized with an older scikit-learn version. Keep them unchanged until a model-refresh phase intentionally accepts updated predictions.
- Root-level compatibility modules remain while the app continues its incremental migration into `app/` and `src/`.
