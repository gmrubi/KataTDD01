import unittest
from src.Conjunto import Conjunto


class TestConjunto ( unittest.TestCase ) :
    def test_conjunto_vacio_retornaNone ( self ) :
        conjunto = Conjunto ( [] )
        self.assertIsNone ( conjunto.promedio ( ) )

    def test_conjunto_unElemento_retornaValorUnicoElemento( self ):
        conjunto=Conjunto([5])
        self.assertIsNone(5,conjunto.promedio())
