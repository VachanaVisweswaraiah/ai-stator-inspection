from types import SimpleNamespace

import numpy as np
import pytest

from app import ai_analysis
from src.config.paths import PROJECT_ROOT
from src.services.tree_analysis import (
    GEMINI_BASE_URL,
    GEMINI_MODEL,
    MissingAISecretError,
    TreeAnalysisError,
    build_tree_analysis_messages,
    convert_numpy_values,
    generate_tree_analysis,
    get_gemini_api_key,
)


def test_numpy_values_are_converted_for_json_serialization():
    value = {
        "node": np.int64(4),
        "children": [np.float64(1.5)],
    }

    assert convert_numpy_values(value) == {
        "node": 4,
        "children": [1.5],
    }


def test_tree_analysis_messages_preserve_existing_prompt_contract():
    messages = build_tree_analysis_messages(
        "How many leaves? ",
        {"id": np.int64(1)},
    )

    assert messages[0]["role"] == "system"
    assert '"id": 1' in messages[0]["content"]
    assert "provided decision tree" in messages[0]["content"]
    assert messages[1] == {
        "role": "user",
        "content": (
            "How many leaves? "
            "according to the provided decision tree"
        ),
    }


def test_tree_analysis_uses_configured_gemini_client():
    captured = {}

    class FakeCompletions:
        def create(self, **kwargs):
            captured.update(kwargs)
            return SimpleNamespace(
                choices=[
                    SimpleNamespace(
                        message=SimpleNamespace(content="  answer  ")
                    )
                ]
            )

    class FakeClient:
        def __init__(self, **kwargs):
            captured["client"] = kwargs
            self.chat = SimpleNamespace(
                completions=FakeCompletions()
            )

    answer = generate_tree_analysis(
        "question",
        {"id": 1},
        "secret",
        client_factory=FakeClient,
    )

    assert answer == "answer"
    assert captured["client"] == {
        "api_key": "secret",
        "base_url": GEMINI_BASE_URL,
    }
    assert captured["model"] == GEMINI_MODEL


def test_missing_and_failed_ai_configuration_have_typed_errors():
    with pytest.raises(MissingAISecretError):
        get_gemini_api_key({})

    with pytest.raises(TreeAnalysisError):
        generate_tree_analysis(
            "question",
            {"id": 1},
            "secret",
            client_factory=lambda **kwargs: (_ for _ in ()).throw(
                RuntimeError("service unavailable")
            ),
        )


def test_ai_renderer_handles_missing_secret_without_crashing(monkeypatch):
    warnings = []
    monkeypatch.setattr(ai_analysis.st, "session_state", {})
    monkeypatch.setattr(ai_analysis.st, "secrets", {})
    monkeypatch.setattr(ai_analysis.st, "header", lambda *args: None)
    monkeypatch.setattr(
        ai_analysis.st,
        "text_area",
        lambda *args, **kwargs: "question",
    )
    monkeypatch.setattr(ai_analysis.st, "button", lambda *args: True)
    monkeypatch.setattr(ai_analysis.st, "warning", warnings.append)

    ai_analysis.render_tree_analysis(
        {"id": 1},
        "test",
        "Example",
    )

    assert warnings
    assert "not configured" in warnings[0]


def test_streamlit_modules_delegate_to_shared_ai_renderer():
    for relative_path in [
        "main.py",
        "iris_viz.py",
        "steel_faults_viz.py",
        "vw_sample_data_viz.py",
    ]:
        source = (PROJECT_ROOT / relative_path).read_text()

        assert "render_tree_analysis" in source
        assert "from openai import OpenAI" not in source
        assert "st.secrets" not in source
