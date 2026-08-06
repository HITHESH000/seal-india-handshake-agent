import re
import pytest
import generator

MAX_WORDS = 80

def contains_single_word_instruction(text: str) -> bool:
    t = text.lower()
    return ("exactly one word" in t) or ("one word only" in t) or ("one word" in t) or ("single word" in t)

def test_count_words_and_limit():
    # Build a sample prompt for each domain and ensure it is <= MAX_WORDS
    for domain in generator.DOMAINS:
        statement = generator.choose_statement(domain)
        prompt = generator.build_prompt(domain, statement)
        assert generator.count_words(prompt) <= MAX_WORDS, f"Prompt for {domain} exceeds {MAX_WORDS} words"

def test_prompt_contains_label_and_domain():
    for domain in generator.DOMAINS:
        statement = generator.choose_statement(domain)
        prompt = generator.build_prompt(domain, statement)
        assert generator.LABEL in prompt
        assert f"[domain:{domain}]" in prompt

def test_prompt_requests_single_word():
    # Ensure generated prompts explicitly ask for a single-word answer
    for domain in generator.DOMAINS:
        statement = generator.choose_statement(domain)
        prompt = generator.build_prompt(domain, statement)
        assert contains_single_word_instruction(prompt), "Prompt does not instruct single-word answer"

def test_build_prompt_truncation_behaviour():
    # Create an artificially long statement and ensure build_prompt either truncates or raises a ValueError
    long_statement = " ".join(["word"] * 200)
    domain = list(generator.DOMAINS.keys())[0]
    try:
        prompt = generator.build_prompt(domain, long_statement)
        assert generator.count_words(prompt) <= MAX_WORDS
    except ValueError:
        # Acceptable fallback behavior if truncation can't make it <= MAX_WORDS
        pytest.skip("Truncation could not produce a prompt within the limit; ensure template size is reviewed")

def test_list_domains_output(capsys):
    # Ensure the list_domains helper prints something sensible
    generator.list_domains()
    captured = capsys.readouterr()
    assert "-" in captured.out or len(captured.out.strip()) > 0

def test_unknown_domain_choice_raises():
    with pytest.raises(KeyError):
        generator.choose_statement("nonexistent-domain")
