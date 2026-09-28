import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
HINDSIGHT_BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)

if not HINDSIGHT_API_KEY:
    raise ValueError("HINDSIGHT_API_KEY is not configured.")

client = Hindsight(
    base_url=HINDSIGHT_BASE_URL,
    api_key=HINDSIGHT_API_KEY
)


BANK_ID = "loanguard-ai"


def create_memory_bank():
    return client.create_bank(
        bank_id=BANK_ID,
        name="LoanGuard AI"
    )


def store_memory(content: str):
    return client.retain(
        bank_id=BANK_ID,
        content=content
    )


def recall_memory(query: str):
    return client.recall(
        bank_id=BANK_ID,
        query=query
    )


def reflect_on_memory(question: str):
    response = client.reflect(
        bank_id=BANK_ID,
        query=question
    )

    return response.text


def get_learning_summary():
    response = client.reflect(
        bank_id=BANK_ID,
        query=(
            "Summarize the important patterns learned from the loan "
            "applications stored in memory. Focus on repayment behavior, "
            "risk indicators, positive factors, and lessons that could "
            "help analyze future loan applications."
        )
    )

    return response.text