from fastapi import FastAPI, HTTPException
from app.models.change_model import ChangeRequest
from app.services.rule_engine import validate_change
from app.services.risk_engine import calculate_risk
from app.services.ai_service import generate_summary
from app.services.history_service import find_similar_changes
from loguru import logger
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "AI Change Reviewer is running 🚀"}


@app.post("/analyze-change")
async def analyze_change(change: ChangeRequest):

    if not change.description or not change.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")

    try:
        # ---------------- RULE ENGINE ---------------- #
        issues, _, breakdown = validate_change(change)

        # ---------------- RISK ENGINE ---------------- #
        risk, score = calculate_risk(breakdown)

        # ---------------- SIMILARITY ENGINE ---------------- #
        similar_cases = find_similar_changes(change.description)

        # ---------------- AI SUMMARY ---------------- #
        summary = "AI skipped"

        if not getattr(change, "skip_ai", False):
            try:
                trimmed_description = change.description[:1000]

                summary = await asyncio.to_thread(
                    generate_summary,
                    trimmed_description,
                    similar_cases   # ✅ pass once (no duplicate work)
                )

            except Exception as ai_error:
                logger.error(f"AI Summary failed: {ai_error}")
                summary = "AI unavailable (timeout/network issue)"

        else:
            summary = "AI skipped in bulk mode"

        return {
            "summary": summary,
            "risk_level": risk,
            "risk_score": score,
            "issues": issues,
            "breakdown": breakdown,
            "similar_cases": similar_cases
        }

    except Exception as e:
        logger.exception("Error during change analysis")
        raise HTTPException(status_code=500, detail=str(e))