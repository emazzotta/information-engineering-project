import math
import re
import xml.etree.ElementTree as ET
from nltk.corpus import stopwords


def clean_text(query):
    query = re.sub(r'[^a-zA-Z0-9 ]', '', query)
    query = re.sub(r'\s+', ' ', query)
    query = query.lower()
    query = query.strip()
    return query


def parse_trec(document):
    result = {}
    tree = ET.parse(document)
    root = tree.getroot()
    for doc in root:
        result[doc[0].text] = clean_text(doc[1].text)
    return result


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

    for term_index in term_words.keys():
        for non_term_index, content in non_term_words.items():
            new_distance = int(math.sqrt((term_index-non_term_index)**2))
            prev_distance = content.get('min_distance')
            content['min_distance'] = new_distance if prev_distance is None or prev_distance > new_distance else prev_distance
            non_term_words[non_term_index] = content

    return {data['word']: data['min_distance'] for data in non_term_words.values()}


if __name__ == '__main__':
    search_queries = parse_trec('documents/irg_queries.trec')
    search_collections = parse_trec('documents/irg_collection_short.trec')

    word_list = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", "."]
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
