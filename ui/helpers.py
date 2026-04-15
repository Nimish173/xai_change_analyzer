# ui/helpers.py

def get_risk_color(risk):
    if risk in ["HIGH", "CRITICAL"]:
        return "red"
    elif risk == "MEDIUM":
        return "orange"
    else:
        return "green"