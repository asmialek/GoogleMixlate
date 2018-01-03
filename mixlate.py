from googletrans import Translator
import random

"""
Language Code
-------- ----
Afrikaans 	af
Albanian 	sq
Arabic 	    ar
Belarusian 	be
Bulgarian 	bg
Catalan 	ca
Chinese Simplified 	    zh-CN
Chinese Traditional 	zh-TW
Croatian 	hr
Czech 	    cs
Danish 	    da
Dutch 	    nl
English 	en
Estonian 	et
Filipino 	tl
Finnish 	fi
French 	fr
Galician 	gl
German 	de
Greek 	el
Hebrew 	iw
Hindi 	hi
Hungarian 	hu
Icelandic 	is
Indonesian 	id
Irish 	ga
Italian 	it
Japanese 	ja
Korean 	ko
Latvian 	lv
Lithuanian 	lt
Macedonian 	mk
Malay 	ms
Maltese 	mt
Norwegian 	no
Persian 	fa
Polish 	pl
Portuguese 	pt
Romanian 	ro
Russian 	ru
Serbian 	sr
Slovak 	sk
Slovenian 	sl
Spanish 	es
Swahili 	sw
Swedish 	sv
Thai 	th
Turkish 	tr
Ukrainian 	uk
Vietnamese 	vi
Welsh 	cy
Yiddish 	yi
"""

# translator = Translator()
#
# text = translator.translate('Hello there, general!', dest='pl')
# print(text)


def mixup(phrase='Hello World!', steps=5, my_src=None, my_dest=None):
    translator = Translator()

    languages = ["af", "sq", "ar", "be", "bg", "ca", "zh-CN", "zh-TW", "hr",
                 "cs", "da", "nl", "en", "et", "tl", "fi", "fr", "gl", "de",
                 "el", "iw", "hi", "hu", "is", "id", "ga", "it", "ja", "ko",
                 "lv", "lt", "mk", "ms", "mt", "no", "fa", "pl", "pt", "ro",
                 "ru", "sr", "sk", "sl", "es", "sw", "sv", "th", "tr", "uk",
                 "vi", "cy", "yi"]

    path = []

    if not my_src:
        text = translator.translate(phrase)
        temp_src = text.src
    else:
        temp_src = my_src

    if not my_dest:
        my_dest = temp_src

    temp_text = phrase

    for i in range(steps):
        temp_dest = random.choice(languages)
        path.append(temp_dest)
        temp_text = translator.translate(temp_text, src=temp_src, dest=temp_dest)
        # print(temp_text)
        temp_text = temp_text.text
        temp_src = temp_dest

    print(path)
    return translator.translate(temp_text, src=temp_src, dest=my_dest)

text = 'Merry christmas and a happy new year!'
print(text)
print(mixup(phrase=text, steps=20).text)
