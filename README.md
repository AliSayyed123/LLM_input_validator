# LLM-Based Input Validator

This project implements an LLM-powered input validator that validates a user profile JSON
using semantic reasoning instead of hard-coded rules.

All validation logic is delegated to a Large Language Model (LLM).
Python is used only for orchestration and strict output schema enforcement.

---

## Requirements

- Python 3.10+
- OpenAI API key
- Internet access

---

## Setup Instructions

### 1. Create and activate virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate
