import math
import functools


def percentile(n, percent, key=lambda x: x):
    """
    Find the percentile of a list of values.

    @parameter N - is a list of values. Note N MUST BE already sorted.
    @parameter percent - a float value from 0.0 to 1.0.
    @parameter key - optional key function to compute value from each element of N.

    @return - the percentile of the values
    """
    if not n:
        return None
    k = (len(n) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(n[int(k)])
    d0 = key(n[int(f)]) * (c - k)
    d1 = key(n[int(c)]) * (k - f)
    return d0+d1


def min_distance(query, collection):
    search_terms = query.split(' ')
    document_words = collection.split(' ')
    term_words = {}
    non_term_words = {}
    word_index = 0

    for word in document_words:
        word_index += 1
        if word in search_terms:
            term_words[word_index] = word
        else:
            non_term_words[word_index] = {'word': word, 'min_distance': None}

    if term_words:
        for term_index in term_words.keys():
            for non_term_index, content in non_term_words.items():
                new_distance = int(math.sqrt((term_index-non_term_index)**2))
                prev_distance = content.get('min_distance')
                content['min_distance'] = new_distance if prev_distance is None or prev_distance > new_distance else prev_distance
                non_term_words[non_term_index] = content
    else:
        for non_term_index, content in non_term_words.items():
            content['min_distance'] = len(non_term_words)
            non_term_words[non_term_index] = content

    return dict({data['word']: data['min_distance'] for data in non_term_words.values()}, **{term_word: 0 for term_word in term_words.values()})
