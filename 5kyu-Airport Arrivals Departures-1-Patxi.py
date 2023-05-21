def flap_display(lines, rotors):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    result = []

    for i in range(len(lines)):
        line = lines[i]
        rotor = rotors[i]
        new_line = ""
        shift = 0

        for j in range(len(line)):
            index = ALPHABET.index(line[j])
            shift += rotor[j]
            new_index = (index + shift) % len(ALPHABET)
            new_line += ALPHABET[new_index]

        result.append(new_line)

    return result
