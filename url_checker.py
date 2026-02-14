import re

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "secure",
    "account", "bank", "confirm"
]

SHORTENERS = [
    "bit.ly", "tinyurl.com", "t.co", "goo.gl"
]

def check_url(url):
    score = 0

    # Too many dots
    if url.count('.') > 4:
        score += 1

    # IP address instead of domain
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 2

    # Suspicious keywords
    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            score += 1

    # Very long URL
    if len(url) > 75:
        score += 1

    # Shortened URL
    for short in SHORTENERS:
        if short in url:
            score += 2

    return score
