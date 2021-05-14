import array
import socket
import sys

def checksum(data):
    if len(data) % 2:
        data += b'\x00'
    check_sum = 0
    for i in range(0, len(data))[::2]:
        check_sum += int.from_bytes(data[i:i + 2], byteorder=sys.byteorder, signed=False)

    while (check_sum >> 16) > 0:
        check_sum = (check_sum & 0xffff) + (check_sum >> 16)
    return ~check_sum & 0xffff
