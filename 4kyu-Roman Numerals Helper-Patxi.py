class RomanNumerals:
    @staticmethod
    def to_roman(num):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        result = ""
        for value, symbol in zip(values, symbols):
            while num >= value:
                result += symbol
                num -= value
        return result

    @staticmethod
    def from_roman(s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0
        for symbol in s[::-1]:
            curr_value = values[symbol]
            if prev_value > curr_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        return result
