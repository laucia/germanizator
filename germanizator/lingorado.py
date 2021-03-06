from lxml import html
import requests
import re
import random
from .germanification import cleanup_german


IPA_TO_GERMAN = {
    'ɔ': ['o'],
    'ʤ': ['j'],
    'ʌ': ['a'],
    's': ['ß'],
    't': ['t'],
    'k': ['k'],
    'ʊ': ['uh'],
    '0': ['ö'],
    'j': ['i'],
    'm': ['m'],
    'z': ['s'],
    'ð': ['d'],
    'v': ['w'],
    'b': ['b'],
    'ʧ': ['tsch'],
    'ə': ['ö', 'e', 'a'],
    'θ': ['d', 't'],
    'X': ['ch'],
    'o': ['o'],
    'ɜ': ['ä'],
    'h': ['h'],
    'ɑ': ['ah'],
    'i': ['ie'],
    'ɪ': ['i'],
    'g': ['g'],
    'r': ['r'],
    'ɛ': ['ä'],
    'l': ['l'],
    'T': ['t'],
    'æ': ['ä', "e"],
    'f': ['v'],
    'Q': ['qu'],
    'ŋ': ['ng'],
    'p': ['p'],
    'n': ['n'],
    'P': ['p'],
    'y': ['ü'],
    'u': ['u'],
    'a': ['a'],
    'd': ['d'],
    'w': ['u'],
    'ʃ': ['sch'],
    'e': ['e'],
    'ɒ': ['a'],
    'ː': ['h', 'r'],
}

weak_schwa = re.compile(r'\(ə\)')


def english_to_ipa(phrase):
    """Transforms a phrase in English to IPA

        :param: phrase: some text
        :return: an array of IPA characters per word

    """
    url = "http://lingorado.com/ipa/"
    data = {
        'output_dialect': 'am',
        'text_to_transcribe': phrase,
    }
    response = requests.post(url, data=data)
    if response.status_code != requests.codes.ok:
        return word
    tree = html.fromstring(response.content)
    ipa = tree.xpath('//div[@id="transcr_output"]/span/text()')
    ipa = " ".join(ipa)
    ipa = weak_schwa.sub("ə", ipa)
    return ipa


def ipa_to_german(word):
    symbols = list(word)
    letters = [
        random.choice(IPA_TO_GERMAN[symbol]) if symbol in IPA_TO_GERMAN else symbol
        for symbol in symbols
    ]
    return "".join(letters)


def english_to_deutsch(sentence):
    return cleanup_german(ipa_to_german(english_to_ipa(sentence)))
