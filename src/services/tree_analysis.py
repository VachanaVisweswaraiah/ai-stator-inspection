import json

from openai import OpenAI


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GEMINI_MODEL = "gemini-3-flash-preview"


class MissingAISecretError(ValueError):
    pass


class TreeAnalysisError(RuntimeError):
    pass


def get_gemini_api_key(secrets):
    try:
        api_key = secrets["api_keys"]["gemini"]
    except Exception as exc:
        raise MissingAISecretError(
            "Gemini API key is not configured."
        ) from exc

    if not api_key:
        raise MissingAISecretError("Gemini API key is not configured.")
    return api_key


def convert_numpy_values(value):
    if isinstance(value, dict):
        return {
            key: convert_numpy_values(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [convert_numpy_values(item) for item in value]
    if hasattr(value, "item"):
        return value.item()
    return value


def build_tree_analysis_messages(prompt, tree_json):
    cleaned_tree = convert_numpy_values(tree_json)
    tree_text = json.dumps(cleaned_tree, indent=2)
    system_prompt = (
        "You are an AI specializing in analysing JSON-based decision trees. "
        "Your task is to answer user questions based only with the provided "
        "decision tree below.\n\n"
        "Here is the decision tree:\n"
        + tree_text
        + "You should only give the answer from the context of the provided "
        "decision tree.\n\n "
        "DO not provide the json structure and id in the answer. Let it be a "
        "natural language and do not use the word json or id in the answer"
    )
    return [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": prompt + "according to the provided decision tree",
        },
    ]


def generate_tree_analysis(
    prompt,
    tree_json,
    api_key,
    client_factory=OpenAI,
):
    if not api_key:
        raise MissingAISecretError("Gemini API key is not configured.")

    try:
        client = client_factory(
            api_key=api_key,
            base_url=GEMINI_BASE_URL,
        )
        response = client.chat.completions.create(
            model=GEMINI_MODEL,
            messages=build_tree_analysis_messages(prompt, tree_json),
        )
        return response.choices[0].message.content.strip()
    except MissingAISecretError:
        raise
    except Exception as exc:
        raise TreeAnalysisError(
            "AI analysis could not be generated."
        ) from exc


__all__ = [
    "GEMINI_BASE_URL",
    "GEMINI_MODEL",
    "MissingAISecretError",
    "TreeAnalysisError",
    "build_tree_analysis_messages",
    "convert_numpy_values",
    "generate_tree_analysis",
    "get_gemini_api_key",
]
