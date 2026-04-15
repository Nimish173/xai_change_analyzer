from pydantic import BaseModel

class ChangeRequest(BaseModel):
    description: str
    has_code_change: bool
    has_rollback_plan: bool
    performance_test_status: str  # "done", "waived", "not_done"
    approver_role: str           # "L4", "SLT"
    skip_ai: bool = False