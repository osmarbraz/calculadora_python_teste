import unittest

#Modulo a testar
from modulo.calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

    def test_soma(self):
        print("Teste soma")
        
        calculadora = Calculadora()

        resultadoEsperado = 15
        
        resultadoCalculado = calculadora.getSoma(10,5)
        
        self.assertEqual(resultadoEsperado,resultadoCalculado)
        
    def test_diferenca(self):
        print("Teste diferença")
        
        calculadora = Calculadora()

        resultadoEsperado = 5
        
        resultadoCalculado = calculadora.getDiferenca(10,5)
        
        self.assertEqual(resultadoEsperado,resultadoCalculado)
        
    def test_produto(self):
        print("Teste produto")
        
        calculadora = Calculadora()

        resultadoEsperado = 50
        
        resultadoCalculado = calculadora.getProduto(10,5)
        
        self.assertEqual(resultadoEsperado,resultadoCalculado)                

    def test_quociente(self):
        print("Teste quociente")
        
        calculadora = Calculadora()

        resultadoEsperado = 2
        
        resultadoCalculado = calculadora.getQuociente(10,5)
        
        self.assertEqual(resultadoEsperado,resultadoCalculado)        

if "__main__" == __name__:
    print("Rodando testes calculadora")
    unittest.main()
    
   