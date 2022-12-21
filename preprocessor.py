import pickle


def get_words(n=6):
    with open('/usr/share/dict/words') as dictionary:
        words = dictionary.read().splitlines()

        """create a dict, with len of words as key and word as value
        save each dict keys in separate pickle file"""
        words_dict = {}
        for word in words:
            if len(word) not in words_dict:
                words_dict[len(word)] = [word]
            else:
                words_dict[len(word)].append(word)

        for key, value in words_dict.items():
            with open(f'words/{key}.pickle', 'wb') as f:
                pickle.dump(value, f)


if __name__ == '__main__':
    # get_words()

    """read pickle file and print words"""
    with open('words/24.pickle', 'rb') as f:
        words = pickle.load(f)
    print(words)
