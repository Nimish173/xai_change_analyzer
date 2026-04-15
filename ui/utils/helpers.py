# ui/utils/helpers.py

import pandas as pd


def get_risk_color(risk):
    if risk in ["HIGH", "CRITICAL"]:
        return "red"
    elif risk == "MEDIUM":
        return "orange"
    return "green"


def to_bool(val):
    return str(val).strip().lower() in ["yes", "y", "true", "1"]


def get_value(row, possible_cols):
    for col in possible_cols:
        if col in row and pd.notna(row[col]):
            return str(row[col]).strip()
    return ""