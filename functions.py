import string
from typing import Dict

numbers = [1, 2, 3]


def keywordargs(**kwargs: string) -> object:
    for key, value in kwargs.items():
        print(key, value)
    print(*numbers)


def keywordargs2(trainer="alex"):
    print(trainer)


kursteilnehmer: dict[str, str] = {'python': 'Spät'}

keywordargs(trainer="alex", **kursteilnehmer)
trainer={'trainer': 'ignaz'}
keywordargs2(**trainer);

# keywordargs("alex")
