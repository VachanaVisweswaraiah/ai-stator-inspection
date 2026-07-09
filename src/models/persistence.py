from pathlib import Path

import joblib


def save_model_artifact(model, path: Path):
    joblib.dump(model, path)


__all__ = ["save_model_artifact"]
