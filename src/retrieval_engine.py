import re
import xml.etree.ElementTree as ET

import nltk
from nltk.corpus import stopwords

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

    # id: search query id, value: list of search collection texts
    query_collection_store = remove_n_percentile_most_farthest_words(0.9, search_collections, search_queries)

    # TF-IDF
    print("TF-IDF")


def remove_n_percentile_most_farthest_words(n, search_collections, search_queries):
    query_collection_store = {}
    for search_query_id, search_query_text in search_queries.items():
        specific_collection = []
        for search_collection_id, search_collection_text in search_collections.items():
            distances = min_distance(search_query_text, search_collection_text)
            worst_percentile = int(percentile(sorted(distances.values()), percent=n))
            new_words = ' '.join([word for word in search_collection_text.split(' ') if distances[word] <= worst_percentile])
            if len(new_words) != len(search_collection_text):
                print('Change detected!')
                print(f'Search query: {search_query_text}')
                print(f'Search collection: {search_collection_text}')
            specific_collection.append(new_words)
        query_collection_store[search_query_id] = specific_collection
    return query_collection_store


if __name__ == '__main__':
    retrieve_results()
