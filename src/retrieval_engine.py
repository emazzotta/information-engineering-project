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
    # TODO: Eliminate stop of collections (at some point)
    pass

    # search_terms = query.split(' ')
    # document_words = collection.split(' ')

    # words_distance = []

    # word_id = 0
    # for word in document_words:
    #     word_id = word_id + 1
    #     words_distance.
    #     # print(f'Current word: {current_word}')
    #     min_distance = 0
    #     for iterate_word in document_words:
    #         # print(f'Iterating: {iterate_word}')
    #         min_distance += 1
    #         if iterate_word in search_terms:
    #             min_distance = 0
    #             print(f'=== {iterate_word} is in search terms')
    #     words_distance.append({'word': current_word, 'distance': min_distance})


if __name__ == '__main__':
    search_queries = parse_trec('documents/irg_queries.trec')
    search_collections = parse_trec('documents/irg_collection_short.trec')
    print("hello")

    word_list = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", "."]
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    print(filtered_words)
