#!/usr/bin/python3

import sys
import argparse
from encoder_decoder import encode_decode
from trainer import train
from hackerman import hack

parser = argparse.ArgumentParser(description='Encryptor parser')
subparsers = parser.add_subparsers()

encode_parser = subparsers.add_parser('encode')
encode_parser.set_defaults(command='encode')
encode_parser.add_argument('--input-file', default=sys.stdin)
encode_parser.add_argument('--output-file', default=sys.stdout)
encode_parser.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
encode_parser.add_argument('--key', required=True)

decode_parser = subparsers.add_parser('decode')
decode_parser.set_defaults(command='decode')
decode_parser.add_argument('--input-file', default=sys.stdin)
decode_parser.add_argument('--output-file', default=sys.stdout)
decode_parser.add_argument('--cipher', required=True, choices=['caesar', 'vigenere'])
decode_parser.add_argument('--key', required=True)

train_parser = subparsers.add_parser('train')
train_parser.set_defaults(command='train')
train_parser.add_argument('--model-file', required=True)
train_parser.add_argument('--text-file', required=True)

hack_parser = subparsers.add_parser('hack')
hack_parser.set_defaults(command='hack')
hack_parser.add_argument('--model-file', required=True)
hack_parser.add_argument('--input-file', default=sys.stdin)
hack_parser.add_argument('--output-file', default=sys.stdout)


if __name__ == '__main__':
    args = vars(parser.parse_args())
    command = args['command']
    files_to_close = []

    try:
        input_file = args.get('input_file')
        output_file = args.get('output_file')
        if isinstance(input_file, str):
            input_file = open(input_file, 'r')
            files_to_close.append(input_file)

        if isinstance(output_file, str):
            output_file = open(output_file, 'w')
            files_to_close.append(output_file)

        if command in ['encode', 'decode']:
            if not args['cipher']:
                raise ValueError('Cipher must be specified')

            encode_decode(
                input_file,
                output_file,
                args['cipher'],
                args['key'],
                decode=command == 'decode'
            )

        elif command == 'train':
            model_file = args['model_file']
            if not model_file:
                raise ValueError('"model-file" must be specified for command train')
            model_file = open(model_file, 'w')
            files_to_close.append(model_file)

            text_file = args['text_file']
            if not text_file:
                raise ValueError('"text-file must be specified for command train')
            text_file = open(text_file, 'r')
            files_to_close.append(text_file)

            train(text_file, model_file)

        elif command == 'hack':
            model_file = args['model_file']
            if not model_file:
                raise ValueError('"model-file" should be specified for command hack')

            model_file = open(model_file, 'r')
            files_to_close.append(model_file)
            hack(input_file, output_file, model_file)

    except ValueError as e:
        print(e)
    finally:
        for file in files_to_close:
            file.close()
