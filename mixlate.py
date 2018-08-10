from googletrans import Translator
import progressbar
import random

languages = {'Afrikaans': 'af',
             'Albanian': 'sq',
             'Arabic': 'ar',
             'Belarusian': 'be',
             'Bulgarian': 'bg',
             'Catalan': 'ca',
             'Chinese Simplified': 'zh-CN',
             'Chinese Traditional': 'zh-TW',
             'Croatian': 'hr',
             'Czech': 'cs',
             'Danish': 'da',
             'Dutch': 'nl',
             'English': 'en',
             'Estonian': 'et',
             'Filipino': 'tl',
             'Finnish': 'fi',
             'French': 'fr',
             'Galician': 'gl',
             'German': 'de',
             'Greek': 'el',
             'Hebrew': 'iw',
             'Hindi': 'hi',
             'Hungarian': 'hu',
             'Icelandic': 'is',
             'Indonesian': 'id',
             'Irish': 'ga',
             'Italian': 'it',
             'Japanese': 'ja',
             'Korean': 'ko',
             'Latvian': 'lv',
             'Lithuanian': 'lt',
             'Macedonian': 'mk',
             'Malay': 'ms',
             'Maltese': 'mt',
             'Norwegian': 'no',
             'Persian': 'fa',
             'Polish': 'pl',
             'Portuguese': 'pt',
             'Romanian': 'ro',
             'Russian': 'ru',
             'Serbian': 'sr',
             'Slovak': 'sk',
             'Slovenian': 'sl',
             'Spanish': 'es',
             'Swahili': 'sw',
             'Swedish': 'sv',
             'Thai': 'th',
             'Turkish': 'tr',
             'Ukrainian': 'uk',
             'Vietnamese': 'vi',
             'Welsh': 'cy',
             'Yiddish': 'yi'}


def mixup(phrase='Hello World!', steps=5, my_src=None, my_dest=None):
    """Hello!

    Args:
        phrase (str): Lol
        steps:
        my_src:
        my_dest:

    Returns:

    """
    translator = Translator()

    path = []

    if not my_src:
        text = translator.translate(phrase)
        temp_src = text.src
    else:
        temp_src = my_src

    if not my_dest:
        my_dest = temp_src

    temp_text = phrase

    bar = progressbar.ProgressBar()

    for i in bar(range(steps)):
        temp_key = random.choice(list(languages.keys()))
        temp_dest = languages[temp_key]
        path.append(translator.translate(temp_key, src='en', dest=my_dest).text.capitalize())
        temp_text = translator.translate(temp_text, src=temp_src, dest=temp_dest)
        # print(temp_text)
        temp_text = temp_text.text
        temp_src = temp_dest

    return translator.translate(temp_text, src=temp_src, dest=my_dest).text, path

if __name__ == '__main__':
    text = 'Wesołych Świąt i szczęśliwego Nowego Roku!'
    translation, path = mixup(phrase=text, my_src='pl', steps=25)
    print(text)
    i = 0
    for item in path:
        i += 1
        print(item + '   ', end='')
    print('\n' + translation)
