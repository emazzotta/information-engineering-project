import re
import xml.etree.ElementTree as ET

import nltk
from nltk.corpus import stopwords
from nltk.text import TextCollection

from src.math_tools import min_distance, percentile


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


def eliminate_stopwords(search_collections):
    nltk.download('stopwords')
    for key, value in search_collections.items():
        filtered = ' '.join([word for word in value.split(' ') if word not in stopwords.words('english')])
        search_collections[key] = filtered
    return search_collections


def retrieve_results():
    search_queries = parse_trec('documents/irg_queries.trec')
    search_collections = parse_trec('documents/irg_collection_short.trec')
    search_collections = eliminate_stopwords(search_collections)

    search_queries = {1: 'lol test', 2: 'test'}
    search_collections = {200: 'haha the sky is so lol blue', 300: 'lol this is a test', 400: 'hmm test'}

    # TF-IDF
    queries_scores = {}
    for search_query_id, search_query_text in search_queries.items():
        terms = search_query_text.split(' ')
        documents = remove_n_percentile_most_farthest_words(search_collections, search_query_text, n=0.9)
        document_scores = {}
        search_texts_collection = TextCollection(documents.values())
        for document_id, document_text in documents.items():
            for term in terms:
                current_score = document_scores.get(document_id, 0.0)
                document_scores[document_id] = current_score + search_texts_collection.tf_idf(term, document_text)
        queries_scores[search_query_id] = document_scores

    print("hello")


def remove_n_percentile_most_farthest_words(search_collections, query_text, n):
    result = {}
    for search_collection_id, search_collection_text in search_collections.items():
        distances = min_distance(query_text, search_collection_text)
        worst_percentile = int(percentile(sorted(distances.values()), percent=n))
        new_words = ' '.join([word for word in search_collection_text.split(' ') if distances[word] <= worst_percentile])
        result.update({search_collection_id: new_words})
    return result


if __name__ == '__main__':
    retrieve_results()
