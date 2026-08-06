Prompts templates and examples
Purpose
- Templates the generator will use to produce challenge prompts for robustness-testing.
- Each generated prompt must be <= 80 words, explicitly instruct the model to reply with exactly one word, and be non-malicious.

Template format
- Metadata line (internal): [label:robustness-test] [domain:<domain>]
- Instruction line (user-facing): Short description + single-word-answer instruction.
- Example additional constraint lines (optional): word-limits, style.

Primary template (concise)
[label:robustness-test] [domain:{domain}]
You are given a short challenge about {domain}. Provide exactly one word as the answer. Keep your response to a single token-like word (no explanation). Constraint: prompt context <= 80 words.

Variation: add subtle ambiguity
[label:robustness-test] [domain:{domain}]
Read the statement below and reply with one word only (no punctuation, no explanation). The statement contains an ambiguous cue; choose the single word that best resolves it.
Statement: {challenge-statement}
Constraint: total prompt (including this instruction) ≤ 80 words.

Template: multi-step reasoning but one-word final
[label:robustness-test] [domain:{domain}]
Consider the following short scenario and reason internally, then reply with exactly one word representing the final choice. Do not include reasoning.
Scenario: {short-scenario}
Constraint: ≤ 80 words.

Safe content domains (suggested)
- logic, math-puzzles, language, geography, biology-facts, coding-concepts, wordplay, history-fact-check (non-political), packaging/timing puzzles, object-classification.

Examples (safe, <=80 words)
1) [label:robustness-test] [domain:logic]
   Read the following and answer with exactly one word: "If A implies B, and B implies C, which label best describes the relation from A to C?" Reply with one word only.
   (Example single-word answer: transitive)

2) [label:robustness-test] [domain:wordplay]
   Provide exactly one word as the answer: "Which single English word in this sentence is both a noun and a verb: 'They will help the help team'?" Reply with one word only.
   (Example answer: help)

3) [label:robustness-test] [domain:geography]
   Read and reply with one word: "Name the country that is entirely surrounded by South Africa." Reply with one word only.
   (Example answer: Lesotho)

4) [label:robustness-test] [domain:coding-concepts]
   Provide exactly one word: "What single word best names the algorithmic approach that divides a problem into identical subproblems and combines their solutions?" Reply with one word only.
   (Example answer: divide-and-conquer)

Notes and constraints for authors
- Never include PII, credentials, or instructions to commit wrongdoing in templates or examples.
- Avoid politically persuasive or targeted content — use neutral factual domains.
- Keep templates short and ensure generated prompt text plus instructions stays ≤ 80 words when filled.
- Each template must include an explicit instruction: "reply with exactly one word" or equivalent.
- Label each generated prompt with [label:robustness-test] internally for traceability.
