import binascii


def hex_encode(string):
    return binascii.b2a_hex(string.encode()).decode()


def hex_decode(string):
    return binascii.a2b_hex(string.encode()).decode()
