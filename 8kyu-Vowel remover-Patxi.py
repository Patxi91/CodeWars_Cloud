def shortcut(s: str) -> str:
    return ''.join([l for l in s if l not in 'aeiou'])
