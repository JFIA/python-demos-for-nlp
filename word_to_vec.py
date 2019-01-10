from gensim.models import word2vec
from nltk import tokenize
import numpy as np


def build_wordvec(text, size, model):
    vec = np.zeros(size).reshape((1, size))
    count = 1
    for word in text:
        try:
            vec += model[word].reshape((1, size))
            count += 1
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec


def build_feature(vocab_list):
    fail_list = []
    vec_feature = []
    for i in range(len(vocab_list)):
        open('corpus.txt', 'w+', encoding='utf-8').write(vocab_list[i])
        try:
            model = word2vec.Word2Vec(word2vec.LineSentence('corpus.txt'), min_count= 3)
        except RuntimeError as e:
            print(e)
            fail_list.append(i)
        else:
            print('第{}轮'.format(i))
            vect = build_wordvec(tokenize.word_tokenize(vocab_list[i]), 100, model)
            vec_feature.append(list(vect[0]))
    return vec_feature
