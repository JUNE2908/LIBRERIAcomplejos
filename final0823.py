import trabajo0823 as pop
import unittest

class TestpopOperations (unittest, TestCase):
    def test_sumacpop(self):
        suma = lc.sumacpop(c1 = (2,3),c2 = (4,5))
        self.assertAlmostEqual(suma[0], 6)
        self.assertAlmostEqual(suma[1], 8)

        suma = lc.sumacpop(c1 = (6,5),c2 = (7,5))
        self.assertAlmostEqual(suma[0], 13)
        self.assertAlmostEqual(suma[1], 10)

    def test_restacpop(self):
        resta = lc.restcpop(c1 = (8,2),c2 = (7,6))
        self.assertAlmostEqual(resta[0], 0)
        self.assertAlmostEqual(resta[1], 30)

        resta = lc.restcpop(c1 = (1,4),c2 = (7,9))
        self.assertAlmostEqual(resta[0], -6)
        self.assertAlmostEqual(resta[1], -5)

    def test_produccpop(self):
        producto = lc.produccpop(c1 = (3,6),c2 = (4,2))
        self.assertAlmostEqual(producto[0], 1)
        self.assertAlmostEqual(producto[1], -4)

        producto = lc.produccpop(c1 = (12,6),c2 = (-5,1))
        self.assertAlmostEqual(producto[0], -66)
        self.assertAlmostEqual(producto[1], -18)


    def test_divicpop(self):
        division = lc.divicpop(c1 = (6,6),c2 = (2,7))
        self.assertAlmostEqual(dividir[0], 0.58, places=1)
        self.assertAlmostEqual(dividir[1], -0.35, places=1)

        division = lc.divicpop(c1 = (2,5),c2 = (2,-4.6))
        self.assertAlmostEqual(dividir[0], 0.02, places=1)
        self.assertAlmostEqual(dividir[1], 0.42, places=1)
        

    def test_modulocpop(self):
        modulo = lc.modulocpop((3,4))
        self.assertAlmostEquasl(modulo,  5.0, places=1)

        modulo = lc.modulocpop((5,12))
        self.assertAlmostEquasl(modulo,  13.0, places=1)

    def test_conjucpop(self):
        conjugado = lc.conjucpop((3,4))
        self.assertAlmostEqual(conjugado[0] , 3)
        self.assertAlmostEqual(conjugado[1] ,-4)

        conjugado = lc.conjucpop((-4,-9))
        self.assertAlmostEqual(conjugado[0] , -4)
        self.assertAlmostEqual(conjugado[1] ,9)
    
            



















        
            
