import pickle

import typer
from rich import print
from rich.prompt import Prompt


def get_words(n=6) -> dict[int, list[str]]:
    """open pickle file based on n and return list of words"""
    file_name = f'words/{n}.pickle'
    with open(file_name, 'rb') as f:
        words = pickle.load(f)
    return words


def print_words(words: list):
    more = True
    start, stop = 0, 10

    while more:
        for word in words[start:stop]:
            print(word)

        more = typer.confirm("need more?")
        start, stop = stop, stop + 10




def wordle(words: list[str], containing: str, not_containing: str):  # , specific_postions: Dict[int, str] = None):

    if containing and not_containing:
        words = [word for word in words if all(letter in word for letter in containing) and
                 all(letter not in word for letter in not_containing)]

    return words


def main(n: int = 6):
    words = get_words(n=6)

    containing = ''
    not_containing = ''

    while len(words) != 1:
        words = wordle(words, containing, not_containing)
        print_words(words)

        containing = Prompt.ask("Enter letters to contain: ", default=containing)
        not_containing = Prompt.ask("Enter letters to [bold] not [/bold] contain: ", default=not_containing)

    print(words)


if __name__ == '__main__':
    typer.run(main)
