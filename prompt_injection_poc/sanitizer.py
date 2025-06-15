import re
from typing import List
BLOCKLIST: List[str] = [
    r"ignore previous instructions",
    r"jailbreak",
]
def sanitize(prompt: str) -> str:
    """Remove suspicious phrases from the prompt and log them."""
    clean = prompt
    for pattern in BLOCKLIST:
        if re.search(pattern, clean, flags=re.IGNORECASE):
            print(f"Blocked phrase detected: {pattern}")
            clean = re.sub(pattern, "", clean, flags=re.IGNORECASE)
    return clean.strip()
