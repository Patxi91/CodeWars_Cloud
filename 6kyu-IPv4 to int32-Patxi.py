import socket
import struct


def ip_to_int32(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]
