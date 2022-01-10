def computer_to_phone(numbers):
    phone = {"0": "0", "1": "7", "2": "8", "3": "9", "4": "4", "5": "5", "6": "6", "7": "1", "8": "2", "9": "3"}
    return ''.join([phone[c] for c in numbers])
