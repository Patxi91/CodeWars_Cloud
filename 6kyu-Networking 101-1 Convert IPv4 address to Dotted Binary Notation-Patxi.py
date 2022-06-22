def ipv4_to_binary(ipv4_addr: str) -> str:
    return '.'.join('{0:08b}'.format(int(x)) for x in ipv4_addr.split('.'))
