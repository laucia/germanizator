import re

germanifications = [
    (
        "accents",
        re.compile(r'[ˈˌ]'),
        r''
    ),
    (
        "initial eszett",
        re.compile(r'\bß'),
        r's'
    ),
    (
        "eszett before consonant",
        re.compile(r'([^aeiouäöü])ß'),
        r'\1s'
    ),
    (
        "eszett before vowel",
        re.compile(r'ß([aeiouäöü])'),
        r's\1'
    ),
    (
        "initial u",
        re.compile(r'\bu'),
        r'w'
    ),
    (
        "initial semiconsonant i",
        re.compile(r'\bi([aeiouäöü])'),
        r'j\1'
    ),
    (
        "final j",
        re.compile(r'j\b'),
        r'ge'
    ),
    (
        "break ai diphtong",
        re.compile(r'ai'),
        r'ahi',
    ),
    (
        "final w",
        re.compile(r'w\b'),
        r'we'
    ),
    (
        "öu",
        re.compile(r'öu'),
        r'o'
    ),
    (
        "double h",
        re.compile(r'hh'),
        r'h'
    ),
    (
        "final consonant cluster bl",
        re.compile(r'bl\b'),
        r'bel',
    ),
    (
        "final consonant cluster wd",
        re.compile(r'wd\b'),
        r'wed',
    ),
    (
        "final consonant cluster pl",
        re.compile(r'pl\b'),
        r'pel',
    ),
]

space_before_punctuation = re.compile(r'( )+([.,?!;])')
two_spaces = re.compile(r'  ')  # weird space-like character

def cleanup_german(phrase):
    result = phrase
    for _, regexp, replacement in germanifications:
        result = regexp.sub(replacement, result)
    # Redo punctuation
    result = space_before_punctuation.sub(r'\2', result)
    result = two_spaces.sub(r' ', result)
    return result
