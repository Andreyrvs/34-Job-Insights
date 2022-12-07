from src.pre_built.counter import count_ocurrences


def test_counter():
    'Retorna contagem de palavras'

    path = "data/jobs.csv"
    word_python = 1639
    wrong_word_python = 9999999
    word_javascript = 122
    wrong_word_javascript = 999
    assert count_ocurrences(path, "Python") == word_python
    assert count_ocurrences(path, "Python") != wrong_word_python
    assert count_ocurrences(path, "Javascript") == word_javascript
    assert count_ocurrences(path, "Javascript") != wrong_word_javascript
