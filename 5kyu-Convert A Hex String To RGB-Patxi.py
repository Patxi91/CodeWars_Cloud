def hex_string_to_RGB(hex_string):
    return {'r':tuple(int((hex_string.lstrip('#'))[i:i+len(hex_string.lstrip('#'))//3], 16) for i in range(0, len(hex_string.lstrip('#')), len(hex_string.lstrip('#'))//3))[0], 'g':tuple(int((hex_string.lstrip('#'))[i:i+len(hex_string.lstrip('#'))//3], 16) for i in range(0, len(hex_string.lstrip('#')), len(hex_string.lstrip('#'))//3))[1], 'b':tuple(int((hex_string.lstrip('#'))[i:i+len(hex_string.lstrip('#'))//3], 16) for i in range(0, len(hex_string.lstrip('#')), len(hex_string.lstrip('#'))//3))[2]}
