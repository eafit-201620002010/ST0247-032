"""
    @clase pruebas
    Descripcion: pruebas con unitary test para el punto 1
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""
import DigraphAL, DigraphAM, unittest
from Lab04 import punto1

class prueba(unittest.TestCase):

    def prueba_punto1(self):
        graph2 = DigraphAL.digraphAL(4)
        graph2.add_arc(0, 1, 20)
        graph2.add_arc(0, 2, 42)
        graph2.add_arc(0, 3, 35)
        graph2.add_arc(1, 0, 20)
        graph2.add_arc(1, 2, 30)
        graph2.add_arc(1, 3, 34)
        graph2.add_arc(2, 0, 42)
        graph2.add_arc(2, 1, 30)
        graph2.add_arc(2, 3, 12)
        graph2.add_arc(3, 0, 35)
        graph2.add_arc(3, 1, 34)
        graph2.add_arc(3, 2, 12)
        self.assertEqual(prueba_punto1(graph2, 0), [0, 1, 2, 3, 0])
        return

    def prueba2_punto1(self):
        graph = DigraphAM.digraphAM(4)
        graph.add_arc(0, 1, 20)
        graph.add_arc(0, 2, 42)
        graph.add_arc(0, 3, 35)
        graph.add_arc(1, 0, 20)
        graph.add_arc(1, 2, 60)
        graph.add_arc(1, 3, 34)
        graph.add_arc(2, 0, 42)
        graph.add_arc(2, 1, 30)
        graph.add_arc(2, 3, 12)
        graph.add_arc(3, 0, 35)
        graph.add_arc(3, 1, 34)
        graph.add_arc(3, 2, 12)
        self.assertEqual(prueba2_punto1(graph, 0), [0, 1, 3, 2, 0])
        return

if  __name__ == '__main__':
    unittest.main()