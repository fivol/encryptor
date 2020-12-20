import json
from io import StringIO

from config import MAX_ALPHABET_SIZE
from encoder_decoder import caesar_cipher_encrypt
from trainer import generate_model_from_text
from utils import shift_char


def model_value_similarity(value1, value2):
    return abs(value1 - value2) ** 2


def model_similarity_metric(curr_model, base_model, curr_model_shift=0):
    return sum(
        model_value_similarity(value, base_model.get(shift_char(char, curr_model_shift), 0))
        for char, value in curr_model.items()
    )


def hack(input_file, output_file, model_file):
    model_file_text = model_file.read()
    model = json.loads(model_file_text)

    best_shift = None
    best_models_similarity = float('inf')

    text = input_file.read()
    encrypted_text_model = generate_model_from_text(text)

    for i in range(MAX_ALPHABET_SIZE):
        models_similarity = model_similarity_metric(encrypted_text_model, model, curr_model_shift=i)

        if models_similarity < best_models_similarity:
            best_models_similarity = models_similarity
            best_shift = i

    best_decrypted_text = StringIO()
    caesar_cipher_encrypt(StringIO(text), best_decrypted_text, best_shift)
    output_file.write(best_decrypted_text.getvalue())
