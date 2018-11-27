import re
import xml.etree.ElementTree as ET


def clean_text(query):
    query = re.sub(r'[^a-zA-Z0-9 ]', '', query)
    query = re.sub(r'\s+', ' ', query)
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
    search_queries = parse_trec('documents/irg_queries.trec')
    search_collections = parse_trec('documents/irg_collection.trec')
    print("hello")
