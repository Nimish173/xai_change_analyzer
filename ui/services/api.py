# ui/services/api.py

import requests

# ✅ SAME session (proxy bypass)
session = requests.Session()
session.trust_env = False

BACKEND_URL = "http://127.0.0.1:8000"


def analyze_change(payload):
    try:
        response = session.post(
            f"{BACKEND_URL}/analyze-change",
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            return {"error": f"{response.status_code} - {response.text}"}

        return response.json()

    except Exception as e:
        return {"error": str(e)}