# LLM-Based Input Validator

This project implements an **LLM-powered input validator** that validates a user profile JSON
using **semantic reasoning** instead of hard-coded rules.

All validation logic is delegated to a **Large Language Model (LLM)**.  
Python is used only for orchestration and **strict output schema enforcement**.

---

## Requirements

- Python 3.10+
- OpenAI API key
- Internet access

---

## Setup Instructions

### 1. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate
```

## Project Structure

```text
llm-input-validator/
│
├── validate_user.py        # Orchestrates validation requests to the LLM
├── prompts.py              # Contains prompt templates for validation
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── README.md               # Project documentation
│
└── evals/
    ├── promptfooconfig.yaml  # Config for evaluation framework
    └── testcases.yaml        # Sample test cases for validation
```
### Requirements
# Python 3.10+
# OpenAI API key
# Internet access
# pip

Setup Instructions
Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
Install dependencies
```
```bash
pip install -r requirements.txt
```
Set environment variables

```bash
Edit .env and add your OpenAI API key:
```
env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
Usage
Run the validator on a sample JSON file:

