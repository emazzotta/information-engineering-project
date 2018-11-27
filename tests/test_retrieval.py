from src.retrieval_engine import min_distance


def should_calculate_simple_word_distances():
    search_query = 'z'
    search_collection = 'x y z a b c'
    result = min_distance(search_query, search_collection)
    assert result == {'x': 2, 'y': 1, 'a': 1, 'b': 2, 'c': 3}


def should_calculate_complex_word_distances():
    search_query = '! ? .'
    search_collection = 'x y ! ? b c this is a test i mean cmon .'
    result = min_distance(search_query, search_collection)
    assert result == {
        'x': 2, 'y': 1, 'b': 1, 'c': 2, 'this': 3, 'is': 4, 'a': 5, 'test': 4, 'i': 3, 'mean': 2, 'cmon': 1
    }
