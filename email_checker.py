PHISHING_PHRASES = [
    "urgent", "act now", "verify your account",
    "account suspended", "click below",
    "confirm your password"
]

def check_email(text):
    score = 0
    text = text.lower()

    for phrase in PHISHING_PHRASES:
        if phrase in text:
            score += 1

    if "http://" in text or "https://" in text:
        score += 2

    if "dear customer" in text:
        score += 1

    return score
