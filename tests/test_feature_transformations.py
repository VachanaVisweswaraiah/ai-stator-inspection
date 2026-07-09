import pandas as pd

from src.features.clustering import perform_kmeans
from src.features import engineering
from src.features.engineering import compute_fit, count_yes_no


def _manufacturing_rows():
    return pd.DataFrame(
        [
            {
                "ID": 1,
                "box_hole_diameter": 30.0,
                "box_hole_depth": 40.0,
                "cylinder_diameter": 30.0,
                "cylinder_height": 30.0,
                "wire_diameter": 1.7,
                "bed_distance": 0.15,
            },
            {
                "ID": 2,
                "box_hole_diameter": 32.0,
                "box_hole_depth": 40.0,
                "cylinder_diameter": 30.0,
                "cylinder_height": 30.0,
                "wire_diameter": 1.7,
                "bed_distance": 0.15,
            },
            {
                "ID": 3,
                "box_hole_diameter": 30.0,
                "box_hole_depth": 43.0,
                "cylinder_diameter": 30.0,
                "cylinder_height": 30.0,
                "wire_diameter": 1.7,
                "bed_distance": 0.15,
            },
        ]
    )


def test_compute_fit_preserves_current_tolerance_boundaries(monkeypatch):
    monkeypatch.setattr(engineering, "load_fake_data", _manufacturing_rows)

    result = compute_fit()

    assert result["check"].tolist() == ["yes", "no", "no"]
    assert result["ID"].tolist() == [1, 2, 3]


def test_count_yes_no_matches_transformed_rows(monkeypatch):
    monkeypatch.setattr(engineering, "load_fake_data", _manufacturing_rows)

    result, count_yes, count_no = count_yes_no()

    assert len(result) == count_yes + count_no
    assert (count_yes, count_no) == (1, 2)


def test_perform_kmeans_returns_the_streamlit_display_contract():
    data = pd.DataFrame(
        {
            "x": [0.0, 0.1, 0.2, 9.8, 9.9, 10.0],
            "y": [0.0, 0.2, 0.1, 9.9, 10.0, 9.8],
        }
    )

    labels, centers, inertia, cluster_count = perform_kmeans(data, n_clusters=2)

    assert len(labels) == len(data)
    assert set(labels) == {0, 1}
    assert cluster_count == 2
    assert len(centers) == 2
    assert all(len(center) == data.shape[1] for center in centers)
    assert all(value == round(value, 2) for center in centers for value in center)
    assert inertia == round(inertia, 2)
    assert inertia >= 0
