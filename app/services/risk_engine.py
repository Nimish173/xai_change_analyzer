def calculate_risk(breakdown):
    score = sum(item["points"] for item in breakdown)

    # Cap at 100
    score = min(score, 100)

    # Risk level mapping
    if score >= 80:
        risk = "CRITICAL"
    elif score >= 60:
        risk = "HIGH"
    elif score >= 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk, score