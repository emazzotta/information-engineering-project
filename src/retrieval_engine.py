import re
import xml.etree.ElementTree as ET


def clean_search_query(query):
    query = re.sub(r'[^a-zA-Z0-9 ]', '', query)
    query = re.sub(r'\s+', ' ', query)
    query = query.strip()
    return query


def parse_search_queries(document):
    queries = {}
    tree = ET.parse(document)
    root = tree.getroot()
    for doc in root:
        queries[doc[0].text] = clean_search_query(doc[1].text)
    return queries


if __name__ == '__main__':
    search_queries = parse_search_queries('documents/irg_queries.trec')
    print("hello")
