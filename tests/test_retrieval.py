from src.retrieval_engine import min_distance


def should_calculate_word_distances():
    search_query = 'z'
    search_collection = 'x y z a b c'
    result = min_distance(search_query, search_collection)
    assert result == {'x': 2, 'y': 1, 'a': 1, 'b': 2, 'c': 3}
