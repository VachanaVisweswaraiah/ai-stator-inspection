import functools as ft
import random

import pandas as pd

from src.data.loaders import load_fake_data


data_model = {
    "Box": {
        "box_hole_diameter": {
            "target_value": 30,
            "min_value": 29.5,
            "max_value": 30.5,
            "factor": 1,
        },
        "box_hole_depth": {
            "target_value": 40,
            "min_value": 36,
            "max_value": 45,
            "factor": 1,
        },
    },
    "Cylinder": {
        "cylinder_diameter": {
            "target_value": 30,
            "min_value": 29.5,
            "max_value": 30.5,
            "factor": 1,
        },
        "cylinder_height": {
            "target_value": 30,
            "min_value": 26,
            "max_value": 36,
            "factor": 1,
        },
    },
    "Wire_dia": {
        "wire_diameter": {
            "target_value": 1.7,
            "min_value": 1.6,
            "max_value": 1.8,
            "factor": 1,
        },
    },
    "Elephant_foot": {
        "bed_distance": {
            "target_value": 0.15,
            "min_value": 0.1,
            "max_value": 0.2,
            "factor": 1,
        }
    },
}


def generate_fake_data(num_rows, process_data_model):
    data = []
    for i in range(num_rows):
        row_data = {"ID": i + 1}
        for param, values in process_data_model.items():
            target_value = values["target_value"]
            min_value = values["min_value"]
            max_value = values["max_value"]
            value = random.normalvariate(
                target_value,
                (max_value - min_value) / 2,
            )
            row_data[param] = value
        data.append(row_data)
    return data


def generate_dataset(num_rows, data_model):
    dfs = []
    for process_data_model in data_model.values():
        df = pd.DataFrame(generate_fake_data(num_rows, process_data_model))
        dfs.append(df)

    df_final = ft.reduce(
        lambda left, right: pd.merge(left, right, on="ID"),
        dfs,
    )
    df_final["Material_seller"] = [
        random.randint(0, 2) for _ in range(len(df_final))
    ]
    return df_final


def create_fake_dataset():
    return generate_dataset(10000, data_model)


def compute_fit():
    df_1 = load_fake_data()
    error_allowances = {
        "box_hole_diameter": (
            data_model["Box"]["box_hole_diameter"]["target_value"],
            2,
        ),
        "box_hole_depth": (
            data_model["Box"]["box_hole_depth"]["target_value"],
            3,
        ),
        "cylinder_diameter": (
            data_model["Cylinder"]["cylinder_diameter"]["target_value"],
            1.5,
        ),
        "cylinder_height": (
            data_model["Cylinder"]["cylinder_height"]["target_value"],
            2.5,
        ),
    }

    for index, row in df_1.iterrows():
        check = "yes"
        for column in df_1.columns:
            if column not in error_allowances:
                continue

            target_value, error_allowance = error_allowances[column]
            if abs(row[column] - target_value) >= error_allowance:
                check = "no"
                break

        df_1.at[index, "check"] = check

    return df_1


def count_yes_no():
    df_1 = compute_fit()
    count_yes = 0
    count_no = 0
    for value in df_1["check"]:
        if value == "yes":
            count_yes += 1
        else:
            count_no += 1
    return df_1, count_yes, count_no

__all__ = [
    "compute_fit",
    "count_yes_no",
    "create_fake_dataset",
    "data_model",
    "generate_dataset",
    "generate_fake_data",
]
