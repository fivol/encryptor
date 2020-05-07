from config import READ_WRITE_BUFFER_SIZE
from utils import shift_char, get_char_num


def caesar_cipher_encrypt(input_stream, output_stream, shift, decode=False):
    if decode:
        shift *= -1

    while True:
        buffer = input_stream.read(READ_WRITE_BUFFER_SIZE)
        output_buffer = ''
        if not buffer:
            break
        for c in buffer:
            output_buffer += shift_char(c, shift)

        output_stream.write(output_buffer)


def vigenere_cipher_encrypt(input_stream, output_stream, key, decode=False):
    key_digits = map(lambda x: get_char_num(x), key)
    if decode:
        key_digits = list(map(lambda x: -x, key_digits))

    j = 0
    while True:
        buffer = input_stream.read(READ_WRITE_BUFFER_SIZE)
        output_buffer = ''
        if not buffer:
            break
        for c in buffer:
            shift = key_digits[j % len(key_digits)]
            output_buffer += shift_char(c, shift)
            j += 1

        output_stream.write(output_buffer)


def encode_decode(input_file, output_file, cipher, key, decode=False):
    available_ciphers = ['caesar', 'vigenere']

    if cipher not in available_ciphers:
        raise ValueError(
            'Cipher can be only {}'.format(' or '.join(list(map(lambda x: f'"{x}"', available_ciphers))))
        )

    if cipher == 'caesar':
        try:
            key = int(key)
            if key == 0:
                print('Warning: key is zero. The cipher is unreliable')

        except ValueError:
            raise ValueError('Key must be a number')

        caesar_cipher_encrypt(input_file, output_file, key, decode=decode)

    elif cipher == 'vigenere':
        vigenere_cipher_encrypt(input_file, output_file, key, decode=decode)
