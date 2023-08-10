def my_first_interpreter(code):
    cell=0
    result=''
    for instr in code:
        if instr =='+':
            if cell == 255:
                cell = 0
            else:
                cell += 1
        if instr == '.':
            result += chr(cell)
    return result
