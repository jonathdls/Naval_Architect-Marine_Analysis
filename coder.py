import binascii


def encode(string):
    return binascii.b2a_hex(string.encode()).decode()


def decode(string):
    return binascii.a2b_hex(string.encode()).decode()
