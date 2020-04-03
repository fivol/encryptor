import argparse
from encoder import encode
from decoder import decode
from trainer import train
from hackerman import hack

parser = argparse.ArgumentParser(description='Encryptor parser')

parser.add_argument('command', type=str, help='Enryption action')
parser.add_argument('--cipher')
parser.add_argument('--input-file')
parser.add_argument('--output-file')
parser.add_argument('--key', default=13)
parser.add_argument('--text-file')
parser.add_argument('--model-file')


if __name__ == '__main__':
    args = vars(parser.parse_args())
    command = args['command']

    try:
        if command in ['encode', 'decode']:
            cipher = args['cipher']
            if cipher not in ['caesar', 'vigenere']:
                raise ValueError('Cipher can be only "caesar" or "vigenere"')

            key = str(args['key'])

            if cipher == 'caesar':
                try:
                    key = int(key)
                    if key == 0:
                        print('Warning: key is zero. The cipher is unreliable')

                except ValueError:
                    raise ValueError('Key must be a number')

            encrypt_func = encode if command == 'encode' else decode
            encrypt_func(args['input_file'], args['output_file'], cipher, key)

        elif command == 'train':
            model_file = args['model_file']
            if not model_file:
                raise ValueError('"model-file" must be specified for command train')

            train(args['text_file'], model_file)

        elif command == 'hack':
            model_file = args['model_file']
            if not model_file:
                raise ValueError('"model-file" should be specified for command hack')

            hack(args['input_file'], args['output_file'], model_file)

    except ValueError as e:
        print(e)
