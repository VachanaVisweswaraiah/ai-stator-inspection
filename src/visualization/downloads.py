from base64 import b64encode
from io import BytesIO

import pandas as pd


def dataframe_to_excel_download_link(
    dataframe,
    filename="data.xlsx",
):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        dataframe.to_excel(
            writer,
            index=False,
            sheet_name="Sheet1",
        )

    encoded_data = b64encode(output.getvalue()).decode()
    return (
        '<a href="data:application/octet-stream;base64,'
        f'{encoded_data}" download="{filename}">'
        "Download Sample Excel file</a>"
    )


__all__ = ["dataframe_to_excel_download_link"]
