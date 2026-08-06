#!/usr/bin/env python3
"""
generator.py

Generate short (<=80-word) challenge prompts labeled for robustness-testing.
Each prompt explicitly instructs the model to reply with exactly one word.

Usage:
    python generator.py                 # prints one sample prompt (auto domain)
    python generator.py --domain math   # prints a prompt in the 'math' domain
    python generator.py --list-domains  # list available domains
"""

from __future__ import annotations
import argparse
import random
import textwrap
import sys

MAX_WORDS = 80
LABEL = "[label:robustness-test]"

# Safe domains and a few example challenge statements per domain.
DOMAINS = {
    "logic": [
        "If A implies B, and B implies C, which single-word label best describes the relation from A to C?",
        "Given 'All swans are white' and 'This bird is a swan', which property applies to that bird? Answer with one word."
    ],
    "math": [
        "What one-word term names the algorithmic approach that divides a problem into identical subproblems and combines their solutions?",
        "Provide one word: the operation that returns the unique value for which f(x)=0 is called what?"
    ],
    "wordplay": [
        "Which single English word can be both a noun and a verb in this sentence: 'They will help the help team'?",
        "Name one word that fits both 'bank' as a financial place and 'bank' as a river edge."
    ],
    "geography": [
        "Name the country that is entirely surrounded by South Africa.",
        "Which one-word name identifies the longest river in the world by common consensus?"
    ],
    "biology": [
        "Provide one word: the cellular process that converts glucose into ATP anaerobically is called what?",
        "One-word answer: what term describes an organism that obtains energy by consuming other organisms?"
    ],
    "coding-concepts": [
        "What single-word term best describes the design that allows an object to take many forms through a common interface?",
        "Provide exactly one word: the technique of finding and fixing defects in software is called what?"
    ]
}

PRIMARY_TEMPLATE = (
    f"{LABEL} [domain:{'{'}domain{'}'}]\n"
    "You are given a short challenge about {domain}. Provide exactly one word as the answer. "
    "Keep your response to a single token-like word (no explanation). "
    "Statement: {statement}\n"
    "Constraint: prompt context <= 80 words."
)

def count_words(text: str) -> int:
    return len(text.strip().split())

def build_prompt(domain: str, statement: str) -> str:
    prompt = PRIMARY_TEMPLATE.format(domain=domain, statement=statement)
    words = count_words(prompt)
    if words <= MAX_WORDS:
        return prompt
    # Try to shorten the statement by truncating to fit
    # Keep the instruction lines intact and shorten the statement.
    allowed_for_statement = MAX_WORDS - (words - len(statement.split()))
    # conservative fallback: take first N words of statement
    statement_words = statement.split()
    if allowed_for_statement <= 0:
        raise ValueError("Unable to build a prompt within the word limit with current template.")
    truncated = " ".join(statement_words[:max(1, allowed_for_statement)])
    prompt = PRIMARY_TEMPLATE.format(domain=domain, statement=truncated)
    if count_words(prompt) <= MAX_WORDS:
        return prompt
    raise ValueError("Could not create a prompt <=80 words even after truncation.")

def choose_statement(domain: str) -> str:
    candidates = DOMAINS.get(domain)
    if not candidates:
        raise KeyError(f"Unknown domain: {domain}")
    return random.choice(candidates)

def list_domains() -> None:
    for d in sorted(DOMAINS.keys()):
        print(f"- {d}")

def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Generate a robustness-test prompt that expects a single-word answer.")
    p.add_argument("--domain", "-d", help="Domain to generate (e.g., logic, math). If omitted, chosen randomly.")
    p.add_argument("--list-domains", action="store_true", help="List available domains and exit.")
    p.add_argument("--seed", type=int, help="Optional random seed for reproducible output.")
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    if args.list_domains:
        list_domains()
        return 0
    if args.seed is not None:
        random.seed(args.seed)
    domain = args.domain if args.domain else random.choice(list(DOMAINS.keys()))
    if domain not in DOMAINS:
        print(f"Error: domain '{domain}' not found. Use --list-domains to see choices.", file=sys.stderr)
        return 2
    statement = choose_statement(domain)
    try:
        prompt = build_prompt(domain, statement)
    except ValueError as e:
        print(f"Error building prompt: {e}", file=sys.stderr)
        return 3
    # Safety: ensure the prompt contains an explicit single-word instruction and the label
    if "one word" not in prompt.lower() and "single word" not in prompt.lower() and "exactly one word" not in prompt.lower():
        print("Error: generated prompt does not explicitly request a single-word answer.", file=sys.stderr)
        return 4
    if count_words(prompt) > MAX_WORDS:
        print("Error: generated prompt exceeds word limit.", file=sys.stderr)
        return 5
    print(prompt)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
