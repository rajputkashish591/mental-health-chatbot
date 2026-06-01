import re

TRIGGER_WORDS = [
    "help",
    "emergency",
    "doctor",
    "hospital",
    "pain",
    "fire",
    "police",
    "suicide",
    "kill myself",
    "accident"
]

def check_emergency(text):

    text = text.lower()

    for word in TRIGGER_WORDS:

        if re.search(r"\b" + re.escape(word) + r"\b", text):

            return True

    return False