import pytest
from minhafuncao import *  

def test_funcao():
    assert soma(10, 10) == 20   
    assert divisao(20, 5) == 4
    assert multi(20, 20) == 400
    assert subtracao(10, 5) == 5

test_funcao()