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


if __name__ == '__main__':
    # Load xml data
    search_queries = parse_trec('documents/irg_queries.trec')
    search_collections = parse_trec('documents/irg_collection_short.trec')

    # Remove stop words in collections
    nltk.download('stopwords')
    for key, value in search_collections.items():
        filtered = ' '.join([word for word in value.split(' ') if word not in stopwords.words('english')])
        search_collections[key] = filtered

    # Remove worst 10%-ile => 90%-ile most farthest
    for search_query_id, search_query_text in search_queries.items():
        for search_collection_id, search_collection_text in search_collections.items():
            distances = min_distance(search_query_text, search_collection_text)
            worst_10_percentile = int(percentile(sorted(distances.values()), percent=0.9))
            new_words = [word for word, distance in distances.items() if distance <= worst_10_percentile]

    print("hello")
