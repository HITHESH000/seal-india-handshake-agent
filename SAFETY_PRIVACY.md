# Safety & Privacy Policy — Handshake AI (SEAL India)

Purpose
- Document safety and privacy rules for the agent and repository.
- Provide clear guidance for contributors and automated checks.

Key rules
- No safety bypass: The agent and all generated prompts must never be designed to circumvent, disable, or exploit model safety systems.
- No malicious content: Do not generate prompts that meaningfully facilitate wrongdoing, violence, illegal activity, or abuse.
- No PII exposure: The agent must never request, store, or return raw personally identifiable information (PII) such as:
  - Full names with identifiers, government IDs, passport numbers, phone numbers, exact addresses
  - Financial account numbers, private keys, or passwords
- Redaction & handling: If a user provides PII accidentally, redact it from logs and escalate to the security contact. Do not include PII in prompts or examples.

Data retention & logging
- Minimal logging: Record only metadata necessary for debugging (timestamp, non-sensitive prompt hash). Do not log API keys, user-provided secrets, or raw PII.
- Retention policy: Remove or redact sensitive content within 30 days and follow organization data-retention policies.

Escalation & reporting
- Escalate safety/privacy incidents immediately to: team-seal@yourorg.example
- Maintain an incident log (SECURITY.md) with anonymized, non-sensitive summaries of incidents and resolution steps.

CI & automated checks
- CI must run:
  - Tests that verify prompt length and single-word-instruction presence.
  - Lightweight safety classifiers (if available) to flag potentially disallowed prompts before they are used in evaluation.
- Secrets: Store any API keys in GitHub Actions secrets; never commit them to the repository.

Contributor responsibilities
- Review PRs that change generation logic or add prompts for safety implications.
- Add tests when modifying generation behavior.
- If unsure whether a prompt is safe, mark it `unsafe` in prompts/examples.json and discuss in the PR.

Contact & policy updates
- Security contact: team-seal@yourorg.example
- This policy may be updated; contributors should check it before making changes that affect generation or safety.
