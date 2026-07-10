# Release Verification

The portfolio release is checked against the same Python 3.12 environment used
by continuous integration and Streamlit Community Cloud.

## Automated Checks

Run the complete release gate from the repository root:

```bash
UV_CACHE_DIR=.uv-cache uv lock --check
UV_CACHE_DIR=.uv-cache uv run --python 3.12 pytest
UV_CACHE_DIR=.uv-cache uv run --python 3.12 python -m compileall -q *.py app src clustering streamlit_flow tests ML_Dash_files
git diff --check
```

The test suite verifies:

- required datasets, model artifacts, and deployment files;
- centralized paths and package import boundaries;
- feature transformation and model prediction contracts;
- legacy compatibility imports;
- Streamlit navigation and shared UI configuration;
- execution of `app/streamlit_app.py` through Streamlit's testing runtime.
- whitespace checks that prevent accidental trailing-space or conflict-marker commits.

## Known Warnings

- Committed decision-tree artifacts were created with scikit-learn 1.4.1.post1
  and load under the locked 1.6.1 runtime with a compatibility warning.
- Matplotlib and joblib may report cache or CPU-detection warnings in restricted
  environments.

These warnings do not currently fail the prediction contracts or Streamlit
smoke test. Model artifacts should only be refreshed after prediction changes
are reviewed and accepted.

## Hosted Verification

After creating or redeploying the Streamlit Community Cloud app:

1. Confirm the deployment reaches a healthy state without build errors.
2. Open every sidebar section and confirm its dataset renders.
3. Exercise one prediction in each decision-tree workflow.
4. Confirm clustering controls and visualizations render.
5. Add the optional Gemini secret and verify AI analysis separately.
6. Record the public application URL in `README.md`.
