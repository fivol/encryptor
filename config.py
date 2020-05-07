import string

VERSION = '1.2.0'

READ_WRITE_BUFFER_SIZE = 1024

alphabets = [
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits
]

MAX_ALPHABET_SIZE = max(map(len, alphabets))
