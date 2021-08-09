def int32_to_ip(int32):
    return '.'.join([str(int32 >> (i << 3) & 0xFF) for i in range(4)[::-1]])
