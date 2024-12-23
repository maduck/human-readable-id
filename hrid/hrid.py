import random
from .adjectives import ADJECTIVES
from .nouns import NOUNS, ANIMALS, FLOWERS
from .verbs import VERBS
from .adverbs import ADVERBS


DICTIONARY = {
    'adjective': ADJECTIVES,
    'noun': NOUNS,
    'verb': VERBS,
    'adverb': ADVERBS,
    'number': list(map(str, range(10,99)))
}


class HRID:
    def __init__(self, delimiter='-', hridfmt=('adjective', 'noun', 'verb', 'adverb'), seed=None):
        self.delimiter = delimiter
        self.phrasefmt = list()
        self.random = random.Random(seed)
        for element in hridfmt:
            self.phrasefmt.append(DICTIONARY.get(element, element))

    def generate(self):
        phrases = list()
        for element in self.phrasefmt:
            if isinstance(element, (str)):
                phrases.append(element)
            if isinstance(element, (list)):
                phrases.append(self.random.choice(element))

        return self.delimiter.join(phrases)
