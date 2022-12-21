import pickle
import string
from typing import Dict

import typer


def get_words(n=6):
    """open pickle file based on n and return list of words"""
    file_name = f'words_{n}.pickle'
    with open(file_name, 'rb') as f:
        words = pickle.load(f)
    return words


def get_letters():
    pass


def find_words(words, containing, not_containing, specific_postions):
    return words


def print_words(words: list):
    for word in words:
        print(word)


def wordle(n: int = 6, containing: str = {string.ascii_lowercase},
           not_containing: str = None):  # , specific_postions: Dict[int, str] = None):
    """from a list of words find words containing specified letters"""
    # if specific_positions is None:
    #     specific_positions = {}

    if not_containing is None:
        not_containing = []
    else:
        not_containing = not_containing.split('')

    words = get_words(n)
    words = find_words(words, containing, not_containing)  # , specific_positions)


def main(n: int = 6):
    containing_letters = typer.prompt("Enter letters to contain: ")
    not_containing_letters = typer.prompt("Enter letters to not contain: ")

    words = get_words(n=6)

    while len(words) > 1:
        words = wordle(words, n, containing_letters, not_containing_letters)
        print_words(words)


if __name__ == '__main__':
    typer.run(main)
