import ipaddress


def is_valid_IP(strng: str) -> bool:
    try:
        return isinstance(ipaddress.ip_address(strng), ipaddress.IPv4Address)
    except:
        return False
