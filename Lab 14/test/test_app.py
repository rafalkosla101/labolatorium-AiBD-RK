from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubbleSort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

def test_bsort():
    tab = [3,6,1,9,5,4,2]
    tab_sort = [1,2,3,4,5,6,9]
    got = bubbleSort(tab)
    assert got == tab_sort