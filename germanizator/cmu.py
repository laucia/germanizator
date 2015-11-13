import random
from nltk.corpus import cmudict

from .germanification import cleanup_german


CMU_DICT = cmudict.dict()


ARPABET_TO_GERMAN = {
    "AA": "a",
    "AE": "ä",
    "AH": "ö",
    "AO": "o",
    "AW": "au",
    "AY": "aei",
    "B": "b",
    "CH": "tsch",
    "D": "d",
    "DH": "z",
    "EH": "e",
    "ER": "ö",
    "EY": "ä",
    "F": "v",
    "G": "g",
    "HH": "h",
    "IH": "i",
    "IY": "ie",
    "JH": "dj",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "NG": "ng",
    "OW": "oa",
    "OY": "eu",
    "P": "p",
    "R": "r",
    "S": "ß",
    "SH": "sch",
    "T": "t",
    "TH": "d",
    "UH": "uh",
    "UW": "o",
    "V": "w",
    "W": "u",
    "Y": "j",
    "Z": "s",
    "ZH": "g",
}



def procedure(text):
    words = text.split(" ")

    prononciations = []

    for word in words:
        pron = germanizer(arpabetizer(word))
        if word.title() == word:
            pron = pron.title()

        prononciations.append(pron)


    return cleanup_german(" ".join(prononciations))

def arpabetizer(word):
    """ Transform english words into an array of arpabet phonems or the original
    word if no decomposition was available
    """
    arpabets = CMU_DICT.get(word.lower())

    if arpabets:
        arpabet = random.choice(arpabets)
    else:
        arpabet = "(" + word + ")"

    return arpabet



def germanizer(arpabet):
    """ Transform arpabet phonems into a germanifyied word.
    Ignores already formed words.
    """
    if isinstance(arpabet, str):
        return arpabet

    current = []
    for phone in arpabet:
        # for now disregard intonations
        current.append(ARPABET_TO_GERMAN.get(phone, ARPABET_TO_GERMAN.get(phone[:-1])))
    return ''.join(current)
