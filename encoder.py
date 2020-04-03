import string

from utils import try_close_files


def caesar_cipher_encoder(input_stream, output_stream, shift):

    def shift_char(char):
        if ''.islower():
            min_char = 'a'
            cycle_size = 26
        elif ''.isupper():
            min_char = 'A'
            cycle_size = 26
        elif ''.isdigit():
            min_char = '0'
            cycle_size = 10
        else:
            return char

        return chr((ord(char) - ord(min_char) + shift) % cycle_size + ord(min_char))

    while True:
        c = input_stream.read(1)
        if not c:
            break

        output_stream.write(shift_char(c))


def vigenere_cipher_encoder(input_stream, output_stream, key):
    pass


def encode(input_file, output_file, cipher, key):
    print('ENCODE', input_file, output_file, cipher, key)

    available_ciphers = ['caesar', 'vigenere']

    if cipher not in available_ciphers:
        raise ValueError(
            'Cipher can be only {}'.format(' or '.join(list(map(lambda x: f'"{x}"', available_ciphers))))
        )

    input_stream = None
    output_stream = None

    try:
        input_stream = open(input_file, 'r')
        output_stream = open(output_file, 'w')

        if cipher == 'caesar':
            try:
                key = int(key)
                if key == 0:
                    print('Warning: key is zero. The cipher is unreliable')

            except ValueError:
                raise ValueError('Key must be a number')

            caesar_cipher_encoder(input_stream, output_stream, key)

        elif cipher == 'vigenere':
            vigenere_cipher_encoder(input_stream, output_stream, key)

    except Exception as e:
        try_close_files(input_stream, output_stream)

        raise e
