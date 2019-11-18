#!venv/bin/python3.7

import argparse
from random import randrange

from google.cloud import translate_v2 as translate

ENGLISH = 'en'


class DodgyTranslator:
    def __init__(self):
        self.client = translate.Client()

    def translate_text(self, text, steps):
        chain = self._language_chain(steps)

        for (source, target) in chain:
            result = self.client.translate(text, target, source_language=source)
            text = result['translatedText']
            print(text)

    def _get_languages(self):
        supported_languages = self.client.get_languages()
        languages = [language['language'] for language in supported_languages]
        return languages

    def _language_chain(self, steps):
        languages = self._get_languages()
        selected_languages = [ENGLISH] + [languages[randrange(0, len(languages))] for _ in range(steps)] + [ENGLISH]
        print(selected_languages)
        pairs = list(zip(selected_languages[:-1], selected_languages[1:]))
        return pairs


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='the text to be translated', type=str)
    parser.add_argument('--steps', help='the number of translation steps to make', type=int, default=5)
    args = parser.parse_args()

    text = args.text
    steps = args.steps

    if len(text) == 0:
        print('Text must not be empty')
        exit(1)
    if steps < 1:
        print('Must have at least 1 step')
        exit(2)
    if steps > 20:
        print('Must have at most 20 steps')
        exit(3)

    dodgy_translator = DodgyTranslator()
    dodgy_translator.translate_text(text, steps)
