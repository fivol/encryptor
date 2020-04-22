from io import StringIO
import json

from config import ALPHABET_SIZE
from encoder_decoder import caesar_cipher_encrypt
from trainer import generate_model_from_text


def model_value_similarity(value1, value2):
    return abs(value1 - value2) ** 2


def model_similarity_metric(curr_model, base_model):
    return sum(
        map(
            lambda char: model_value_similarity(curr_model[char],
                                                base_model.get(char, 0)),
            curr_model
        )
    )

def hack(input_file, output_file, model_file):
    model_file_text = model_file.read()
    model = json.loads(model_file_text)

    best_decrypted_text = ''
    best_models_similarity = 999999999

    text = input_file.read()
    for i in range(ALPHABET_SIZE):
        input_stream = StringIO(text)
        output_stream = StringIO()

        caesar_cipher_encrypt(input_stream, output_stream, i, decode=True)
        decrypted_text = output_stream.getvalue()
        decrypted_text_model = generate_model_from_text(decrypted_text)
        models_similarity = model_similarity_metric(decrypted_text_model, model)

        if models_similarity < best_models_similarity:
            best_models_similarity = models_similarity
            best_decrypted_text = decrypted_text

    output_file.write(best_decrypted_text)
