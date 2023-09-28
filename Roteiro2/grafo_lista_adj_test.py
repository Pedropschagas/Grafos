import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        # Grafo Questão 2
        self.q2 = MeuGrafo()
        self.q2.adiciona_vertice("A")
        self.q2.adiciona_vertice("B")
        self.q2.adiciona_vertice("C")
        self.q2.adiciona_vertice("D")
        self.q2.adiciona_vertice("E")
        self.q2.adiciona_vertice("F")
        self.q2.adiciona_vertice("G")
        self.q2.adiciona_vertice("H")
        self.q2.adiciona_vertice("I")
        self.q2.adiciona_vertice("J")
        self.q2.adiciona_vertice("K")
        self.q2.adiciona_aresta('a01', 'A', 'B')
        self.q2.adiciona_aresta('a02', 'A', 'G')
        self.q2.adiciona_aresta('a03', 'A', 'J')
        self.q2.adiciona_aresta('a04', 'G', 'K')
        self.q2.adiciona_aresta('a05', 'K', 'J')
        self.q2.adiciona_aresta('a06', 'G', 'J')
        self.q2.adiciona_aresta('a07', 'J', 'I')
        self.q2.adiciona_aresta('a08', 'I', 'G')
        self.q2.adiciona_aresta('a09', 'G', 'H')
        self.q2.adiciona_aresta('a10', 'H', 'F')
        self.q2.adiciona_aresta('a11', 'F', 'B')
        self.q2.adiciona_aresta('a12', 'G', 'B')
        self.q2.adiciona_aresta('a13', 'B', 'C')
        self.q2.adiciona_aresta('a14', 'C', 'D')
        self.q2.adiciona_aresta('a15', 'D', 'E')
        self.q2.adiciona_aresta('a16', 'B', 'D')
        self.q2.adiciona_aresta('a17', 'B', 'E')

        # Arvore DFS Grafo PB
        self.a_dfs = MeuGrafo()
        self.a_dfs.adiciona_vertice("J")
        self.a_dfs.adiciona_vertice("C")
        self.a_dfs.adiciona_vertice("E")
        self.a_dfs.adiciona_vertice("P")
        self.a_dfs.adiciona_vertice("M")
        self.a_dfs.adiciona_vertice("T")
        self.a_dfs.adiciona_vertice("Z")
        self.a_dfs.adiciona_aresta('a1', 'J', 'C')
        self.a_dfs.adiciona_aresta('a2', 'C', 'E')
        self.a_dfs.adiciona_aresta('a4', 'C', 'P')
        self.a_dfs.adiciona_aresta('a6', 'C', 'T')
        self.a_dfs.adiciona_aresta('a8', 'M', 'T')
        self.a_dfs.adiciona_aresta('a9', 'T', 'Z')

        # Arvore BFS Grafo PB
        self.a_bfs = MeuGrafo()
        self.a_bfs.adiciona_vertice("J")
        self.a_bfs.adiciona_vertice("C")
        self.a_bfs.adiciona_vertice("E")
        self.a_bfs.adiciona_vertice("P")
        self.a_bfs.adiciona_vertice("M")
        self.a_bfs.adiciona_vertice("T")
        self.a_bfs.adiciona_vertice("Z")
        self.a_bfs.adiciona_aresta('a1', 'J', 'C')
        self.a_bfs.adiciona_aresta('a2', 'C', 'E')
        self.a_bfs.adiciona_aresta('a4', 'C', 'P')
        self.a_bfs.adiciona_aresta('a6', 'C', 'T')
        self.a_bfs.adiciona_aresta('a7', 'C', 'M')
        self.a_bfs.adiciona_aresta('a9', 'T', 'Z')

        # Arvore DFS Grafo Questão 2
        self.b_dfs = MeuGrafo()
        self.b_dfs.adiciona_vertice("A")
        self.b_dfs.adiciona_vertice("B")
        self.b_dfs.adiciona_vertice("C")
        self.b_dfs.adiciona_vertice("D")
        self.b_dfs.adiciona_vertice("E")
        self.b_dfs.adiciona_vertice("F")
        self.b_dfs.adiciona_vertice("G")
        self.b_dfs.adiciona_vertice("H")
        self.b_dfs.adiciona_vertice("I")
        self.b_dfs.adiciona_vertice("J")
        self.b_dfs.adiciona_vertice("K")
        self.b_dfs.adiciona_aresta("a01", "A", "B")
        self.b_dfs.adiciona_aresta("a11", "B", "F")
        self.b_dfs.adiciona_aresta("a10", "F", "H")
        self.b_dfs.adiciona_aresta("a09", "H", "G")
        self.b_dfs.adiciona_aresta("a04", "G", "K")
        self.b_dfs.adiciona_aresta("a05", "K", "J")
        self.b_dfs.adiciona_aresta("a07", "J", "I")
        self.b_dfs.adiciona_aresta("a13", "B", "C")
        self.b_dfs.adiciona_aresta("a14", "C", "D")
        self.b_dfs.adiciona_aresta("a15", "D", "E")

        # Arvore BFS Grafo Questão 2
        self.b_bfs = MeuGrafo()
        self.b_bfs.adiciona_vertice("A")
        self.b_bfs.adiciona_vertice("B")
        self.b_bfs.adiciona_vertice("C")
        self.b_bfs.adiciona_vertice("D")
        self.b_bfs.adiciona_vertice("E")
        self.b_bfs.adiciona_vertice("F")
        self.b_bfs.adiciona_vertice("G")
        self.b_bfs.adiciona_vertice("H")
        self.b_bfs.adiciona_vertice("I")
        self.b_bfs.adiciona_vertice("J")
        self.b_bfs.adiciona_vertice("K")
        self.b_bfs.adiciona_aresta("a01", "A", "B")
        self.b_bfs.adiciona_aresta("a02", "A", "G")
        self.b_bfs.adiciona_aresta("a03", "A", "J")
        self.b_bfs.adiciona_aresta("a11", "B", "F")
        self.b_bfs.adiciona_aresta("a13", "B", "C")
        self.b_bfs.adiciona_aresta("a16", "B", "D")
        self.b_bfs.adiciona_aresta("a17", "B", "E")
        self.b_bfs.adiciona_aresta("a10", "H", "F")
        self.b_bfs.adiciona_aresta("a04", "G", "K")
        self.b_bfs.adiciona_aresta("a08", "G", "I")

        # Arvore DFS grafo desconexo
        self.c_dfs = MeuGrafo()
        self.c_dfs.adiciona_vertice("A")
        self.c_dfs.adiciona_vertice("B")
        self.c_dfs.adiciona_aresta("asd", 'A', 'B')

        # Arvore BFS grafo desconexo
        self.c_bfs = MeuGrafo()
        self.c_bfs.adiciona_vertice("A")
        self.c_bfs.adiciona_vertice("B")
        self.c_bfs.adiciona_aresta("asd", 'A', 'B')

        # Arvore DFS grafo PB Sem paralelas
        self.d_dfs = MeuGrafo()
        self.d_dfs.adiciona_vertice('J')
        self.d_dfs.adiciona_vertice('C')
        self.d_dfs.adiciona_vertice('E')
        self.d_dfs.adiciona_vertice('P')
        self.d_dfs.adiciona_vertice('M')
        self.d_dfs.adiciona_vertice('T')
        self.d_dfs.adiciona_vertice('Z')
        self.d_dfs.adiciona_aresta('a1', 'J', 'C')
        self.d_dfs.adiciona_aresta('a2', 'C', 'E')
        self.d_dfs.adiciona_aresta('a3', 'C', 'P')
        self.d_dfs.adiciona_aresta('a4', 'C', 'T')
        self.d_dfs.adiciona_aresta('a6', 'T', 'M')
        self.d_dfs.adiciona_aresta('a7', 'T', 'Z')

        # Arvore BFS grafo PB Sem paralelas
        self.d_bfs = MeuGrafo()
        self.d_bfs.adiciona_vertice('J')
        self.d_bfs.adiciona_vertice('C')
        self.d_bfs.adiciona_vertice('E')
        self.d_bfs.adiciona_vertice('P')
        self.d_bfs.adiciona_vertice('M')
        self.d_bfs.adiciona_vertice('T')
        self.d_bfs.adiciona_vertice('Z')
        self.d_bfs.adiciona_aresta('a1', 'J', 'C')
        self.d_bfs.adiciona_aresta('a2', 'C', 'E')
        self.d_bfs.adiciona_aresta('a3', 'C', 'P')
        self.d_bfs.adiciona_aresta('a4', 'C', 'T')
        self.d_bfs.adiciona_aresta('a5', 'C', 'M')
        self.d_bfs.adiciona_aresta('a7', 'T', 'Z')







    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas)
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas)
        self.assertFalse(self.g_c.ha_paralelas)
        self.assertFalse(self.g_c2.ha_paralelas)
        self.assertFalse(self.g_c3.ha_paralelas)
        self.assertTrue(self.g_l1.ha_paralelas)

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    # Teste Grafo Paraiba Raiz 'J'
    def test_dfs(self):
        self.assertEqual(self.g_p.dfs('J'), self.a_dfs)

    def test_bfs(self):
        self.assertEqual(self.g_p.bfs('J'), self.a_bfs)

    # Teste Grafo Q2 Raiz 'A'
    def teste_dfs(self):
        self.assertEqual(self.q2.dfs('A'), self.b_dfs)

    def teste_bfs(self):
        self.assertEqual(self.q2.bfs('A'), self.b_bfs)

    # Teste Grafo Desconexo Raiz 'A'
    def teste_dfs(self):
        self.assertEqual(self.g_d.dfs('A'), self.c_dfs)

    def teste_bfs(self):
        self.assertEqual(self.g_d.bfs('A'), self.c_bfs)

    # Teste grafo PB sem Paralelas Raiz 'J'
    def teste_dfs(self):
        self.assertEqual(self.g_p_sem_paralelas.dfs('J'), self.d_dfs)

    def teste_bfs(self):
        self.assertEqual(self.g_p_sem_paralelas.bfs('J'), self.d_bfs)
