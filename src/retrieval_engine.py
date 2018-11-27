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

    words_info = []

    word_index = 0
    for word in document_words:
        word_index = word_index + 1
        words_info.append({'index': word_index, 'word': word, 'min_distance': None})


if __name__ == '__main__':
    search_queries = parse_trec('documents/irg_queries.trec')
    search_collections = parse_trec('documents/irg_collection_short.trec')

    word_list = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", "."]
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
