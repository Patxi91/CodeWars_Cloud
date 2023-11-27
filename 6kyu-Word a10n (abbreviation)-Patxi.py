def abbreviate(s):
    current_word = ""
    word_list = []
    result_list = []

    for char in s:
        if char.isalpha():
            current_word += char
        else:
            word_list.append(current_word)
            word_list.append(char)
            current_word = ""
            continue

    if current_word:
        word_list.append(current_word)

    for word in word_list:
        if len(word) >= 4:
            result_list += word[0] + str(len(word) - 2) + word[-1]
        else:
            result_list += word

    return "".join(result_list)
