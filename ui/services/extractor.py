# ui/services/extractor.py
from services.excel_parser import extract_text_from_excel, get_column_value
from services.detectors import (
    detect_code_change,
    detect_rollback,
    detect_performance_status,
    detect_approver
)


def process_excel(df):
    text = extract_text_from_excel(df)
    full_text = " ".join(df.astype(str).values.flatten()).lower()

    # Priority: Column → Detection → Default

    # Performance status
    perf = get_column_value(df, "Performance Test Status")
    if not perf:
        perf = detect_performance_status(full_text)

    # Approver role
    approver = get_column_value(df, "Approver Role")
    if not approver:
        approver = detect_approver(full_text)

    # Booleans
    has_code = detect_code_change(full_text)
    has_rollback = detect_rollback(full_text)

    return {
        "description": text,
        "has_code_change": has_code,
        "has_rollback_plan": has_rollback,
        "performance_test_status": perf,
        "approver_role": approver.upper()
    }