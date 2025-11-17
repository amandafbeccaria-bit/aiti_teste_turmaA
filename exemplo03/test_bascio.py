import pytest 
 
@pytest.fixture 
def lista_simples(): 
    return [1,2,3,4,5]

def test_soma(lista_simples):
    assert sum(lista_simples) == 15

def test_lenght(lista_simples):
   assert len(lista_simples) == 5 

def test_primeiro_elemento(lista_simples): 
    assert (lista_simples[0]) == 1

def test_primeiro_elemento(lista_simples): 
    assert (lista_simples[-1]) == 5

def test_3(lista_simples): 
    assert 3 in lista_simples

def test_ordenada(lista_simples): 
    assert (sorted(lista_simples)) == lista_simples


