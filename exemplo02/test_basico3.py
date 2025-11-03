def somar(a,b):
    return a + b 
def comprimento(lista): 
   return len(lista)

def test_comprimento(): 
   assert comprimento([4,5,6]) == 3

def test_somar():
 assert somar(2,3) == 5


def test_somar_e_comprimento():
   assert somar(2,3) == 5 
   assert comprimento([1,2,3,4,5]) == 5 