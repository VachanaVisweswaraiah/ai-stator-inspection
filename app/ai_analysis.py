import streamlit as st

from src.services.tree_analysis import (
    MissingAISecretError,
    TreeAnalysisError,
    generate_tree_analysis,
    get_gemini_api_key,
)


def render_tree_analysis(tree_json, state_key, placeholder):
    answer_key = f"llm_answer_{state_key}"
    if answer_key not in st.session_state:
        st.session_state[answer_key] = None

    st.header("AI-Powered Analysis")
    prompt = st.text_area(
        "Describe your Question:",
        placeholder=placeholder,
        key=f"prompt_input_{state_key}",
    )

    if st.button("Generate AI-Based Analysis"):
        try:
            api_key = get_gemini_api_key(st.secrets)
            answer = generate_tree_analysis(
                prompt,
                tree_json,
                api_key,
            )
        except MissingAISecretError:
            st.warning(
                "AI analysis is unavailable because the Gemini API key "
                "is not configured."
            )
        except TreeAnalysisError as exc:
            st.error(str(exc))
        else:
            if answer:
                st.session_state[answer_key] = answer

    if st.session_state[answer_key]:
        st.markdown("### LLM Answer:")
        st.write(st.session_state[answer_key])


__all__ = ["render_tree_analysis"]
