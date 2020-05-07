from collections import Counter
import json


def generate_model_from_text(text):
    text = text.lower()
    counter = dict(Counter(text))
    total = sum(counter.values(), 0.0)
    if not total:
        total = 1

    for key in counter:
        counter[key] /= total

    return counter


def train(text_file, model_file):
    file_text = text_file.read()
    text_model = generate_model_from_text(file_text)
    model_file.write(json.dumps(text_model))
