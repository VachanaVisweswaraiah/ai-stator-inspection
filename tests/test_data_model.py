from data_model import data_model


def test_data_model_contains_expected_process_groups():
    assert set(data_model) == {"Box", "Cylinder", "Wire_dia", "Elephant_foot"}


def test_engineering_parameters_define_numeric_ranges():
    for process_name, parameters in data_model.items():
        assert parameters, f"{process_name} must define at least one parameter"

        for parameter_name, values in parameters.items():
            for key in ("target_value", "min_value", "max_value"):
                assert key in values, f"{process_name}.{parameter_name} missing {key}"
                assert isinstance(values[key], (int, float))

            assert values["min_value"] <= values["target_value"] <= values["max_value"]
