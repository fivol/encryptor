#!/usr/bin/python3

import sys
import argparse
from encoder_decoder import encode_decode
from trainer import train
from hackerman import hack

parser = argparse.ArgumentParser(description='Encryptor parser')

parser.add_argument('command', type=str, help='Enryption action')
parser.add_argument('--cipher')
parser.add_argument('--input-file')
parser.add_argument('--output-file')
parser.add_argument('--key', default=13, type=str)
parser.add_argument('--text-file')
parser.add_argument('--model-file')


if __name__ == '__main__':
    args = vars(parser.parse_args())
    command = args['command']
    files_to_close = []

    try:
        input_file = args.get('input_file')
        output_file = args.get('output_file')
        if input_file:
            input_file = open(input_file, 'r')
            files_to_close.append(input_file)
        else:
            input_file = sys.stdin

        if output_file:
            output_file = open(output_file, 'w')
            files_to_close.append(output_file)
        else:
            output_file = sys.stdout

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
