import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.abspath(__file__))

CURRICULUM_PATH = os.path.dirname(dir_path)
DATA_PATH = os.path.join(CURRICULUM_PATH, 'data')

new_words = ['learning', 'yearning', 'killer', 'filler', 'whales', 'shales', 'skiller', 'killers', 'typhon', 'phyton', 'polos', 'pools', 'sloop', 'spool']
words_to_remove = ['letter', 'making', 'getting', 'leather', 'detail', 'mature', 'season', 'leading', 'leader', 'father']


with open(os.path.join(DATA_PATH, 'words_list.txt')) as f:
    words = [word.strip().lower() for word in f.readlines()]
    for word in new_words:
        if word not in words:
            words.append(word)

    for word in words_to_remove:
        if word in words:
            words.remove(word)

    word_list = words

    words_by_letter = defaultdict(list)
    for word in word_list:
        words_by_letter[word[0]].append(word)

    words_by_letter = dict(words_by_letter)
