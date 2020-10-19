import pytest
from ironizator_sentences import ironizator_sentences_def

def test_ironizator_sentences_def():
    result = ironizator_sentences_def("Polska dla Polakow")

    assert result == 'PoLsKa dLa pOlAkOw'
