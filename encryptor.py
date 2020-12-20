#!/usr/bin/python3

import sys
import argparse
from contextlib import suppress
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
            encode_decode(
                input_file,
                output_file,
                args['cipher'],
                args['key'],
                decode=(command == 'decode')
            )

        elif command == 'train':
            with open(args['model_file'], 'w') as model_file:
                with open(args['text_file'], 'r') as text_file:
                    train(text_file, model_file)

        elif command == 'hack':
            with open(args['model_file'], 'r') as model_file:
                hack(input_file, output_file, model_file)

    except ValueError as e:
        print(e)
    finally:
        for file in files_to_close:
            with suppress(Exception):
                file.close()
