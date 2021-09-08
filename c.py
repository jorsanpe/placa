import pprint

from collections import Counter
from pathlib import Path
from collections import Counter


def _analyze(payload, characters, symbols):
    lines = payload.split('\n')
    for line in lines:
        for char in line:
            if char != ' ':
                if char.isalpha():
                    characters[char] += 1
                else:
                    symbols[char] += 1


def analyze(directories):
    characters = Counter()
    symbols = Counter()
    for directory in directories:
        files = list(Path(directory).rglob('*.c')) + list(Path(directory).rglob('*.cc')) + list(Path(directory).rglob('*.cpp'))
        for path in files:
            with open(path, 'r') as stream:
                payload = stream.read()
            _analyze(payload, characters, symbols)
    print(pprint.pformat(symbols))
    print(pprint.pformat(characters))
