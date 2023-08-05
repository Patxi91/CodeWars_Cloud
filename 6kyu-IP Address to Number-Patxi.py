def ip_to_num(ip):
    # Split the IP address into four octets
    octets = ip.split('.')

    # Convert each octet to an integer
    octet_ints = [int(octet) for octet in octets]

    # Calculate the 32-bit number representation
    num = (octet_ints[0] << 24) + (octet_ints[1] << 16) + (octet_ints[2] << 8) + octet_ints[3]

    return num

def num_to_ip(num):
    # Convert the 32-bit number to four octets
    octet1 = (num >> 24) & 255
    octet2 = (num >> 16) & 255
    octet3 = (num >> 8) & 255
    octet4 = num & 255

    # Create the IP address string
    ip_address = f"{octet1}.{octet2}.{octet3}.{octet4}"

    return ip_address
