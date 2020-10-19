import pytest
from ironizator_sentences import ironizator_sentences_def

def test_ironizator_sentences_def():
    result = ironizator_sentences_def("polska dla Polakow", False)
    assert result == 'pOlSkA DlA PoLaKoW'


def test_ironizator_sentences_underscores():
    string="Polska_zyj"
    print("string:" + string)
    result = ironizator_sentences_def(string, True)
    print("result:" + result)
    assert result == "pOlSkA ZyJ"
