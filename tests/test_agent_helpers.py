from app.agent import build_loan_prompt


def test_build_loan_prompt_contains_loan_data():
    loan_data = {
        "applicant_id": "TEST-001",
        "monthly_income": 80000,
        "loan_amount": 500000,
    }

    memories = "Previous applicant had excellent repayment history."

    prompt = build_loan_prompt(loan_data, memories)

    assert "TEST-001" in prompt
    assert "80000" in prompt
    assert "500000" in prompt
    assert "excellent repayment history" in prompt


def test_build_loan_prompt_contains_required_sections():
    loan_data = {
        "applicant_id": "TEST-002",
        "monthly_income": 90000,
        "loan_amount": 600000,
    }

    memories = "Previous loan repayment was good."

    prompt = build_loan_prompt(loan_data, memories)

    assert "Risk observations" in prompt
    assert "Positive factors" in prompt
    assert "Potential concerns" in prompt
    assert "Recommended next action" in prompt