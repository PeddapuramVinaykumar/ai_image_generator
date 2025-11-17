BLOCKED_WORDS = {"nsfw", "porn", "child", "illegal", "bomb", "kill"}

def is_prompt_allowed(prompt: str):
    found = [w for w in BLOCKED_WORDS if w in prompt.lower()]
    return (len(found) == 0, found)
