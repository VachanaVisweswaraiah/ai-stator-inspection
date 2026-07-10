from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def read_source(relative_path: str) -> str:
    return (PROJECT_ROOT / relative_path).read_text()


def test_synthetic_tree_expert_insights_state_is_namespaced():
    source = read_source("main.py")

    assert 'DT_HYPOTHESES_KEY = "submitted_hypotheses_dt"' in source
    assert 'PDT_HYPOTHESES_KEY = "submitted_hypotheses_pdt"' in source
    assert 'PDT_FORM_KEY = "domain_hypothesis_form_pdt"' in source
    assert "st.session_state['node_debug_info_dt']" in source
    assert "st.session_state['node_debug_info_pdt']" in source

    assert 'st.session_state["submitted_hypotheses"]' not in source
    assert "st.session_state['node_debug_info']" not in source


def test_dataset_expert_insight_widgets_use_scoped_keys():
    dataset_modules = {
        "iris_viz.py": "iris",
        "steel_faults_viz.py": "steel_faults",
        "vw_sample_data_viz.py": "vw_sample",
    }

    for module_path, scope in dataset_modules.items():
        source = read_source(module_path)

        assert f'key="domain_hypothesis_form_dt_{scope}"' in source
        assert f'key="hypo_prob_dt_{scope}"' in source
        assert f'key="fail_imp_dt_{scope}"' in source
        assert 'key="domain_hypothesis_form_dt"' not in source
        assert 'key="hypo_prob_dt"' not in source
        assert 'key="fail_imp_dt"' not in source
