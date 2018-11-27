from src.retrieval_engine import min_distance


def should_calculate_word_distances():
    search_queries = {'245': 'z'}
    search_collections = {'543': 'x y z a b c'}
    result = min_distance(search_queries, search_collections)
    assert result == {'x': 2, 'y': 1, 'a': 1, 'b': 2, 'c': 3}
