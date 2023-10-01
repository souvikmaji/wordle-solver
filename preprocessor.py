import pickle


def get_words(n=6):
    with open('/usr/share/dict/words') as dictionary:
        words = {x.lower() for x in dictionary.read().splitlines()}

        """create a dict, with len of words as key and word as value
        save each dict keys in separate pickle file"""
        words_dict = {}
        for word in words:
            score = get_score(word)

            if len(word) not in words_dict:
                words_dict[len(word)] = {score: [word]}
            elif score not in words_dict[len(word)]:
                words_dict[len(word)][score] = [word]
            else:
                words_dict[len(word)][score].append(word)

        for length, values in words_dict.items():
            with open(f'words/{length}.pickle', 'wb') as f:
                word_list = []
                for key in sorted(values.keys(), reverse=True):
                    word_list.extend(values[key])

                pickle.dump(word_list, f)


def get_score(word):
    uniqueness = len(set(word))
    return uniqueness


if __name__ == '__main__':
    get_words()

    """read pickle file and print words"""
    with open('words/6.pickle', 'rb') as f:
        words = pickle.load(f)
    print(words)
