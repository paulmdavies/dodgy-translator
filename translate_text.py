from google.cloud import translate_v2 as translate


def translate_text():
    client = translate.Client()
    supported_languages = client.get_languages()
    languages = [language['language'] for language in supported_languages]
    print(languages)

    results = client.translate(["The cat", "The dog"], 'fr', source_language='en')
    print(results)


if __name__ == '__main__':
    translate_text()
