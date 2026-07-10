import pytest
from streamlit.testing.v1 import AppTest

from app.navigation import SECTIONS
from src.config.paths import PROJECT_ROOT


WORKFLOW_EXPECTATIONS = [
    (
        "Data Understanding",
        "Box and Cylinder Analysis",
        ["Synthetic Dataset", "Box-Cylinder Model Range"],
    ),
    (
        "k-means",
        "Box and Cylinder Analysis",
        [],
    ),
    (
        "Decision Tree",
        "Box and Cylinder Analysis",
        ["Predictions for Synthetic Dataset"],
    ),
    (
        "Probabilistic Decision Tree",
        "Box and Cylinder Analysis",
        ["Predictions for Synthetic Dataset"],
    ),
    (
        "Iris PDT",
        "IRIS Dataset Analysis",
        ["Iris Dataset"],
    ),
    (
        "Steel Faults PDT",
        "Steel Faults Dataset Analysis",
        ["Steel Faults Dataset"],
    ),
    (
        "Volkswagen PDT",
        "Volkswagen Dataset Analysis",
        ["Volkswagen Dataset"],
    ),
]


@pytest.mark.parametrize(
    ("section", "expected_title", "expected_headers"),
    WORKFLOW_EXPECTATIONS,
)
def test_streamlit_workflow_renders_without_exceptions(
    monkeypatch,
    section,
    expected_title,
    expected_headers,
):
    monkeypatch.setenv("STREAMLIT_TEST_SECTION", section)
    app = AppTest.from_file(
        str(PROJECT_ROOT / "tests" / "fixtures" / "streamlit_routed_app.py"),
        default_timeout=60,
    )

    app.run(timeout=60)

    assert not app.exception
    assert [title.value for title in app.title] == [expected_title]

    rendered_headers = [header.value for header in app.header]
    for expected_header in expected_headers:
        assert expected_header in rendered_headers


def test_end_to_end_smoke_suite_covers_every_navigation_workflow():
    covered_sections = {section for section, _, _ in WORKFLOW_EXPECTATIONS}

    assert covered_sections == set(SECTIONS.values())
