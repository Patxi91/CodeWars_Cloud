def sort_by_name(arr):
    # Define a dictionary mapping numbers to their equivalent names
    number_names = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety"
    }

    # Define a function to convert a number to its equivalent name
    def convert_to_name(number):
        if number < 20:
            return number_names[number]
        elif number < 100:
            tens = number // 10 * 10
            ones = number % 10
            if ones == 0:
                return number_names[tens]
            else:
                return number_names[tens] + " " + number_names[ones]
        else:
            hundreds = number // 100
            remainder = number % 100
            if remainder == 0:
                return number_names[hundreds] + " hundred"
            else:
                return number_names[hundreds] + " hundred and " + convert_to_name(remainder)

    # Sort the array by name, using the number as the key for sorting
    sorted_arr = sorted(arr, key=lambda x: convert_to_name(x))

    return sorted_arr
