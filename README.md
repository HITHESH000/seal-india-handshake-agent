# Handshake AI — SEAL India (seal-india-handshake-agent)

Purpose
- Agent to select a domain and generate short challenge prompts (<= 80 words) that require a single-word answer for robustness-testing of models.

Contents
- agent_manifest.yaml — agent metadata and behavior constraints.
- AGENTS.md — repository guidance for Copilot/Agents.
- SAFETY_PRIVACY.md — safety and privacy policy.
- generator.py — prompt generator script.
- prompts/ — templates and examples.
- tests/ — unit tests for generator behavior.
- .github/workflows/ci.yml — CI to run tests and linting.

Quick start (local)
1. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Generate a sample prompt:
   python generator.py
   # or for a domain:
   python generator.py --domain logic

4. Run tests:
   pytest

Repository setup notes
- Add OPENAI_API_KEY (or other provider key) to repository Actions secrets if you plan to use CI evaluation against a model.
- Follow AGENTS.md and SAFETY_PRIVACY.md before adding new prompts or modifying generation logic.

Contributing
- Create a branch for your change, add tests for any generation logic modifications, and open a Pull Request.
- Request at least one reviewer for changes that touch prompt generation or safety policy.

License
- This repository is licensed under the Apache-2.0 License.

Contact
- Security & safety contact: team-seal@yourorg.example
