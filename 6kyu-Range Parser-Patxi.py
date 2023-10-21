def range_parser(s):
    # Helper function to parse a single token
    def parse_token(token):
        parts = token.split('-')
        if len(parts) == 1:
            return [int(parts[0])]
        elif len(parts) == 2:
            start, end = map(int, parts)
            return list(range(start, end + 1))
        return []

    tokens = s.split(',')
    result = []

    for token in tokens:
        if ':' in token:
            parts = token.split(':')
            if len(parts) == 2:
                sub_result = parse_token(parts[0])
                step = int(parts[1])
                sub_result = [x for i, x in enumerate(sub_result) if i % step == 0]
                result.extend(sub_result)
        else:
            result.extend(parse_token(token))

    return result
