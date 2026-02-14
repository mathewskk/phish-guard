def check_domain(domain):
    score = 0

    # Too many hyphens
    if domain.count('-') > 2:
        score += 1

    # Very long domain name
    if len(domain) > 30:
        score += 1

    # Random-looking characters
    if any(char.isdigit() for char in domain):
        score += 1

    return score
