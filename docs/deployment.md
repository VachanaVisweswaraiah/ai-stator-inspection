# Deployment

This project is prepared for Streamlit Community Cloud deployment from the cleaned GitHub repository.

## Streamlit Cloud Settings

- Repository: `VachanaVisweswaraiah/ai-stator-inspection`
- Branch: `main`
- Main file path: `app/streamlit_app.py`
- Python version: `3.12`
- Python dependencies: `requirements.txt`
- System packages: `packages.txt`
- Streamlit config: `.streamlit/config.toml`

## Secrets

The optional AI analysis feature expects this secret in the Streamlit Cloud app settings:

```toml
[api_keys]
gemini = "your-api-key"
```

The app can still load and display the non-AI workflows without committing local secret files. If a visitor requests AI analysis without this secret, the app displays an availability warning instead of failing. Do not commit `.streamlit/secrets.toml`.

## Pre-Deployment Checklist

Before deploying or redeploying:

1. Confirm the latest branch is pushed to GitHub.
2. Confirm GitHub Actions passes on `main`.
3. Confirm the app starts locally:

```bash
uv run streamlit run app/streamlit_app.py
```

4. Confirm the verification suite passes:

```bash
UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest
```

The complete release gate and post-deployment checks are documented in
`docs/release_verification.md`.

## Expected Runtime Assets

The deployment expects the repository-owned datasets and model artifacts to be present in the repository root. Paths are resolved through `src.config.paths`, so the app should not depend on the current working directory when launched through `app/streamlit_app.py`.
