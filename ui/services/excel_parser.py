# ui/services/excel_parser.py
import pandas as pd


def extract_text_from_excel(df: pd.DataFrame) -> str:
    text_parts = []

    for col in df.columns:
        if any(k in col.lower() for k in ["description", "activity", "step", "comment"]):
            text_parts.extend(df[col].dropna().astype(str).tolist())

    return " ".join(text_parts)


def get_column_value(df: pd.DataFrame, column_name: str):
    for col in df.columns:
        if col.lower() == column_name.lower():
            values = df[col].dropna()
            if not values.empty:
                return str(values.iloc[0]).lower()
    return None