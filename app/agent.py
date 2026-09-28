from app.groq_service import ask_groq
from app.hindsight_service import recall_memory, reflect_on_memory, store_memory


def build_loan_prompt(loan_data: dict, memories: str) -> str:
    return f"""
You are LoanGuard-AI, an AI loan decision-support agent.

Use the applicant information and relevant historical memory below.

Applicant information:
{loan_data}

Relevant historical memory:
{memories}

Analyze the application and provide:
1. Risk observations
2. Positive factors
3. Potential concerns
4. Recommended next action

Do not make a final lending decision. Provide decision-support reasoning
that a human reviewer can evaluate.
"""


def analyze_loan(loan_data: dict):
    applicant_text = str(loan_data)

    # Store the current application as memory
    store_memory(
        f"Loan application reviewed: {applicant_text}"
    )

    # Retrieve relevant previous experience
    memories = recall_memory(
        "What previous loan experience or repayment information "
        "is relevant to this applicant?"
    )

    # Ask Hindsight to reflect on accumulated memories
    reflection = reflect_on_memory(
        "What does the stored loan experience tell us about "
        "responsible repayment and risk?"
    )
    memories = f"""
{memories}

Hindsight reflection:
{reflection}
"""

   # Combine retrieved memories and Hindsight reflection
    memories = (
        f"Retrieved memories:\n{memories}\n\n"
        f"Hindsight reflection:\n{reflection}"
    )

    prompt = build_loan_prompt(
        loan_data,
        memories
    )

    return ask_groq(prompt)