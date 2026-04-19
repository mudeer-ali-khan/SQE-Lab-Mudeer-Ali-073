"""
String Utilities Module
SQE Lab Task
"""

def count_vowels(text: str) -> int:
    if text is None:
        raise TypeError
    return sum(1 for c in text.lower() if c in "aeiou")


def reverse_string(text: str) -> str:
    if text is None:
        raise TypeError
    return text[::-1]


def is_palindrome(text: str) -> bool:
    if text is None:
        raise TypeError
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> int:
    if text is None:
        raise TypeError
    return len(text.split())


def capitalise_words(text: str) -> str:
    if text is None:
        raise TypeError
    return " ".join(word.capitalize() for word in text.split())


def remove_duplicates(text: str) -> str:
    if text is None:
        raise TypeError

    result = []
    prev = None

    for ch in text:
        if ch != prev:
            result.append(ch)
        prev = ch

    return "".join(result)
