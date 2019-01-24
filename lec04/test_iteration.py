from iteration import _matches_at, substr_index
# , substr_index2


def test__matches_at():
    assert(_matches_at('a', 'apple', 0))
    assert(not _matches_at('b', 'apple', 0))
    assert(not _matches_at('p', 'apple', 0))
    assert(_matches_at('pl', 'apple', 2))
    assert(_matches_at('ple', 'apple', 2))
    assert(not _matches_at('ples', 'apple', 2))
    assert(_matches_at('', 'apple', 0))
    assert(_matches_at('', 'apple', 1))
    assert(_matches_at('', 'apple', 5))


def test_substr_index():
    assert(substr_index('a', 'apple') == 0)
    assert(substr_index('b', 'apple') is None)
    assert(substr_index('p', 'apple') == 1)
    assert(substr_index('l', 'apple') == 3)
    assert(substr_index('pp', 'apple') == 1)
    assert(substr_index('ppp', 'apple') is None)
    assert(substr_index('pl', 'apple') == 2)
    assert(substr_index('hello', 'h') is None)
    assert(substr_index('', 'apple') == 0)


# def test_substr_index2():
#     assert(substr_index2('a', 'apple') == 0)
#     assert(substr_index2('b', 'apple') is None)
#     assert(substr_index2('p', 'apple') == 1)
#     assert(substr_index2('l', 'apple') == 3)
#     assert(substr_index2('pp', 'apple') == 1)
#     assert(substr_index2('ppp', 'apple') is None)
#     assert(substr_index2('pl', 'apple') == 2)
#     assert(substr_index2('hello', 'h') is None)
#     assert(substr_index2('', 'apple') == 0)
