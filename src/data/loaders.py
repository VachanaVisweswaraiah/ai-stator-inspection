import pandas as pd

from src.config.paths import (
    ENGINEERED_CLUSTER_DATA_PATH,
    ENGINEERING_DATA_PATH,
    FAKE_DATA_PATH,
    IRIS_DATA_PATH,
    PDT_PREDICTED_DATA_PATH,
    PREDICTED_DATA_PATH,
    STEEL_FAULTS_DATA_PATH,
    VW_SAMPLE_DATA_PATH,
)


def load_fake_data():
    return pd.read_excel(FAKE_DATA_PATH)


def load_engineering_data():
    return pd.read_excel(ENGINEERING_DATA_PATH)


def load_engineered_cluster_data():
    return pd.read_excel(ENGINEERED_CLUSTER_DATA_PATH)


def load_predicted_data():
    return pd.read_excel(PREDICTED_DATA_PATH)


def load_pdt_predicted_data():
    return pd.read_excel(PDT_PREDICTED_DATA_PATH)


def load_iris_data():
    return pd.read_csv(IRIS_DATA_PATH)


def load_steel_faults_data():
    return pd.read_csv(STEEL_FAULTS_DATA_PATH)


def load_vw_sample_data():
    return pd.read_csv(VW_SAMPLE_DATA_PATH, sep=";", decimal=",", on_bad_lines="skip")
