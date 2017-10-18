"""
    @clase Pruebas
    Descripcion: Pruebas de los puntos del laboratorio 3
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""
import DigraphAL, DigraphAM, unittest, time
from Laboratorio3 import n_reinas, punto1_3, punto1_6, punto2

class TestQueens(unittest.TestCase):
  
  def test_reinas(self):
    solutions = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
    for i in range(len(solutions)):
      self.assertEqual(n_reinas(i + 1), solutions[i])
  
  def prueba_punto1_3(self):
    g = DigraphAL.digraphAL(12)
    g.add_arc(5, 11,  1)
    g.add_arc(11, 2,  1)
    g.add_arc(11, 9,  1)
    g.add_arc(11, 10, 1)
    g.add_arc(7,  8,  1)
    g.add_arc(7, 11,  1)
    g.add_arc(8,  9,  1)
    g.add_arc(3,  8,  1)
    g.add_arc(3,  10, 1)
    solution_7 = [7, 8, 11, 9, 2, 10]
    solution_5 = [5, 11, 2, 9, 10]
    solution_3 = [3, 8, 10, 9]
    self.assertEqual(punto1_3(g, 7), solution_7)
    self.assertEqual(punto1_3(g, 5), solution_5)
    self.assertEqual(punto1_3(g, 3), solution_3)

  def test_punto1_6(self):
    g = DigraphAL.digraphAL(5)
    g.add_arc(0, 1, 2)
    g.add_arc(1, 0, 2)
    g.add_arc(0, 2, 2)
    g.add_arc(2, 0, 1)
    f = DigraphAL.digraphAL(5)
    f.add_arc(0, 1, 1)
    f.add_arc(1, 2, 1)
    f.add_arc(2, 3, 1)
    f.add_arc(3, 4, 1)
    h = DigraphAL.digraphAL(5)
    h.add_arc(0, 1, 1)
    h.add_arc(0, 0, 1)
    h.add_arc(1, 1, 1)
    h.add_arc(1, 2, 1)
    self.assertEqual(punto1_6(g), True)
    self.assertEqual(punto1_6(f), False)
    self.assertEqual(punto1_6(h), True)

  def test_punto2(self):
    g = DigraphAL.digraphAL(5)
    g.add_arc(0, 1,  3)
    g.add_arc(0, 1,  4)
    g.add_arc(0, 2,  1)
    g.add_arc(2, 3, 15)
    g.add_arc(1, 3,  3)
    self.assertEqual(punto2(g, 0, 3), 6)
    self.assertEqual(punto2(g, 0, 1), 3)

if __name__ == '__main__':
  start = time.clock()
  n_reinas(4)
  end = time.clock() - start
  print("n_reinas:", end * 1000, "ms")
  unittest.main()