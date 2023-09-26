def align_right(text, width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if len(' '.join(current_line + [word])) <= width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line).rjust(width))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line).rjust(width))

    return '\n'.join(lines)
