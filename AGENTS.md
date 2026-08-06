Project: Handshake AI — SEAL India

Purpose
- Provide repo-level guidance to Copilot/Agents and contributors.
- Primary agent task: select a domain and generate a challenge prompt (<= 80 words) that instructs the target model to reply with a single word.
- Testing goal: produce non-malicious, ambiguity- or reasoning-focused prompts used for robustness-testing of models.

Agent behavior & rules
- Always ask the user to confirm a domain if one is not provided. If the user declines, auto-select a reasonable domain.
- Generated prompts must:
  - Be 80 words or fewer (count words separated by whitespace).
  - Explicitly instruct the model to reply using a single word.
  - Be non-malicious and not attempt to bypass model safety.
  - Be labeled internally as "robustness-test".
- Never generate prompts that request or expose raw PII, credentials, or instructions to commit wrongdoing.
- If the user attempts to request bypassing model safety, refuse and provide a safe refusal message.

Coding standards
- Language: Python 3.10+
- Formatting: use black; run flake8 for linting.
- Tests: pytest for unit tests.
- Dependency management: requirements.txt for CI; prefer pinned minimal set.

Development & running locally
- Secrets: Add OPENAI_API_KEY (or equivalent) to repository Actions secrets for CI evaluation.
- To run generator locally:
  - python -m venv .venv
  - source .venv/bin/activate
  - pip install -r requirements.txt
  - python generator.py --mode sample
- Tests:
  - pytest tests/

File responsibilities
- generator.py — domain selection + prompt generation.
- prompts/ — templates and examples used by the generator and tests.
- tests/ — checks for prompt length, single-word-instruction presence, and safety flags.

Safety & escalation
- Do not use generated prompts to attempt to bypass other models’ safety constraints.
- If content suggests potential PII, illegal activity, or harm, escalate to designated contact: team-seal@yourorg.example and log the incident in SECURITY.md.

Contributing & review
- Create a branch per change, open a Pull Request, and request at least one code review.
- All changes that modify generation logic or tests must include new/updated unit tests.
