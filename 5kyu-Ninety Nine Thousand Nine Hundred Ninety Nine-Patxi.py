def number_to_english(n):
    ones_dict = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen'
    }

    tens_dict = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
        8: 'eighty', 9: 'ninety'
    }

    if not isinstance(n, int) or n < 0 or n > 99999:
        return ""

    if n == 0:
        return "zero"

    result = ""

    if n >= 1000:
        thousands = n // 1000
        result += number_to_english(thousands) + " thousand "
        n %= 1000

    if n >= 100:
        hundreds = n // 100
        result += ones_dict[hundreds] + " hundred "
        n %= 100

    if n > 0:
        if n < 20:
            result += ones_dict[n]
        else:
            tens = n // 10
            result += tens_dict[tens]
            n %= 10
            if n > 0:
                result += " " + ones_dict[n]

    return result.strip()
