import unittest
from laboratorio2 import queens

class TestNQueens(unittest.TestCase):

  def test_queens(self):

    soluciones = [1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
    for i in range(len(soluciones)):
      self.assertEqual(queens(i), soluciones[i])
  
if __name__ == '__main__':
  unittest.main()
  