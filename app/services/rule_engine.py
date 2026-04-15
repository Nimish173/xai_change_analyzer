def validate_change(change):
    issues = []
    breakdown = []
    score = 0

    words = change.description.split()
    unique_words = set(words)

    # ---------------- Rule 1: Poor / Short Description ---------------- #
    if len(words) < 10:
        issues.append("Description is too short. Add more details.")
        breakdown.append({
            "rule": "Short Description",
            "points": 20,
            "reason": "Insufficient details increase ambiguity and risk"
        })
        score += 20

    # 🔥 Edge Case: Repetitive / low-quality description
    elif len(unique_words) / len(words) < 0.5:
        issues.append("Description quality is poor (too repetitive).")
        breakdown.append({
            "rule": "Low Quality Description",
            "points": 15,
            "reason": "Repetitive text reduces clarity of the change"
        })
        score += 15

    # ---------------- Rule 2: Missing Rollback ---------------- #
    if not change.has_rollback_plan:
        issues.append("Rollback plan is missing.")
        breakdown.append({
            "rule": "No Rollback Plan",
            "points": 30,
            "reason": "Without rollback, recovery from failure is difficult"
        })
        score += 30

    # ---------------- Rule 3: Code Change without Testing ---------------- #
    if change.has_code_change and change.performance_test_status == "not_done":
        issues.append("Code change without performance testing.")
        breakdown.append({
            "rule": "No Performance Testing",
            "points": 25,
            "reason": "Untested code may cause performance or stability issues"
        })
        score += 25

    # ---------------- Rule 4: Invalid Waiver ---------------- #
    if change.performance_test_status == "waived" and change.approver_role != "SLT":
        issues.append("Performance test waiver must be approved by SLT.")
        breakdown.append({
            "rule": "Invalid Waiver Approval",
            "points": 15,
            "reason": "Improper approval violates governance policies"
        })
        score += 15

    # ---------------- Rule 5: High Risk Keywords ---------------- #
    high_risk_words = ["database", "migration", "production", "downtime"]

    detected_keywords = []
    for word in high_risk_words:
        if word in change.description.lower():
            detected_keywords.append(word)

    if detected_keywords:
        issues.append(f"High risk keywords detected: {', '.join(detected_keywords)}")
        breakdown.append({
            "rule": "High Risk Keywords",
            "points": 10,
            "reason": "Operations like database/migration/production are sensitive"
        })
        score += 10

    return issues, score, breakdown