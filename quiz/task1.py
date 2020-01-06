import binascii

hjjjhjhj
def hex_encode(string):
    """
    Hex encode a string

    Parameters
    ----------
    string : str
        String to be encoded
    Returns
    -------
    str
        Text string with hexadecimal representation of input string
    """
    return binascii.b2a_hex(string.encode()).decode()


def hex_decode(string):
    """
    Hex decode string

    Parameters
    ----------
    string : str
        String to be decoded from hexadecimal
    Returns
    -------
    str
        Text string with ASCII / unicode representation of hexadecimal input string
    """
    return binascii.a2b_hex(string.encode()).decode()
