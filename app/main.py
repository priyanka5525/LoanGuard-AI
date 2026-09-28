from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import analyze_loan
from app.hindsight_service import get_learning_summary


app = FastAPI(
    title="LoanGuard-AI",
    description="Hindsight-powered AI loan decision-support agent",
    version="1.0.0",
)


class LoanApplication(BaseModel):
    applicant_id: str
    age: int
    monthly_income: float
    employment_type: str
    employment_years: float
    loan_amount: float
    loan_purpose: str
    credit_score: int
    existing_monthly_emi: float
    previous_loan_repayment: str
    previous_defaults: int


@app.get("/")
def home():
    return {
        "message": "LoanGuard-AI is running",
        "status": "healthy",
    }


@app.post("/analyze-loan")
def analyze_loan_application(application: LoanApplication):
    try:
        loan_data = application.model_dump()

        print("DEBUG - Loan data received:")
        print(loan_data)

        result = analyze_loan(loan_data)

        print("DEBUG - Analysis generated successfully")

        return {
            "applicant_id": application.applicant_id,
            "analysis": result,
        }

    except Exception as e:
        print("DEBUG - API ERROR:")
        print(type(e)._name_)
        print(str(e))

        return {
            "error_type": type(e)._name_,
            "error_message": str(e),
        }


@app.get("/learning-summary")
def learning_summary():
    return {
        "learning_summary": get_learning_summary()
    }