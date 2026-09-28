# LoanGuard-AI

## Hindsight-Powered AI Loan Decision-Support Agent

LoanGuard-AI is an AI-powered loan decision-support agent built for the
*AI Agents That Learn Using Hindsight* hackathon.

It combines *Hindsight memory* with *Groq LLM reasoning* to analyze loan
applications using both current applicant information and previously stored
loan experience.

> LoanGuard-AI provides decision-support reasoning for human reviewers. It
> does not make a final lending decision.

---

## Problem

Traditional loan-analysis systems often evaluate an application primarily
from the information available at the time of the request.

This makes it difficult to continuously learn from previous application
patterns and repayment experiences.

LoanGuard-AI addresses this by giving the agent a memory layer that can
retain, recall, and reason over previous loan experiences.

---

## Solution

LoanGuard-AI follows this flow:

```text
Loan Application
       |
       v
FastAPI API
       |
       v
LoanGuard-AI Agent
       |
       +--------------------+
       |                    |
       v                    v
Hindsight Memory         Groq LLM
       |                    |
       +---------+----------+
                 |
                 v
          Risk Analysis
                 |
                 v
       Human Reviewer