# ui/services/detectors.py

def detect_code_change(text: str) -> bool:
    keywords = ["code", "script", "deploy", "release"]
    return any(word in text for word in keywords)


def detect_rollback(text: str) -> bool:
    return "rollback" in text or "revert" in text


def detect_performance_status(text: str) -> str:
    if any(word in text for word in ["waived", "skipped"]):
        return "waived"
    elif any(word in text for word in ["not done", "pending"]):
        return "not_done"
    return "done"


def detect_approver(text: str) -> str:
    if "slt" in text:
        return "SLT"
    elif "l4" in text:
        return "L4"
    elif "l3" in text:
        return "L3"
    elif "l2" in text:
        return "L2"
    return "L1"