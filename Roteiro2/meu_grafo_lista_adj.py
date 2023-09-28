from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        arestas = self.arestas
        vert = self.vertices
        n_adj = set()
        for i in vert:
            adj = []
            for j in arestas:
                if arestas[j].v1.rotulo == i.rotulo:
                    v2 = arestas[j].v2.rotulo
                    adj.append(v2)
                elif arestas[j].v2.rotulo == i.rotulo:
                    v1 = arestas[j].v1.rotulo
                    adj.append(v1)
            for l in vert:
                if l.rotulo != i.rotulo and l.rotulo not in adj:
                    if f'{l}-{i.rotulo}' not in n_adj:
                        n_adj.add(f'{i.rotulo}-{l}')
        return n_adj

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        laco = False
        for i in self.arestas:
            if self.arestas[i].v1 == self.arestas[i].v2:
                laco = True
        return laco

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        v_obj = self.get_vertice(V)
        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1 == v_obj:
                grau += 1
            if self.arestas[a].v2 == v_obj:
                grau += 1
        return grau

    @property
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas = self.arestas
        arestas_unicas = {}
        for chave, aresta in arestas.items():
            rotulo_vertice1, rotulo_vertice2 = aresta.v1.rotulo, aresta.v2.rotulo
            aresta_tupla = (rotulo_vertice1, rotulo_vertice2) if rotulo_vertice1 < rotulo_vertice2 else (
            rotulo_vertice2, rotulo_vertice1)
            if aresta_tupla in arestas_unicas:
                return True
            arestas_unicas[aresta_tupla] = True
        return False



    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        todas_as_arestas = self.arestas
        if not self.existe_vertice(self.get_vertice(V)):
            raise VerticeInvalidoError()
        else:
            arestas_incidentes = set()
            for chave_aresta in todas_as_arestas:
                if todas_as_arestas[chave_aresta].v1.rotulo == V or todas_as_arestas[chave_aresta].v2.rotulo == V:
                    arestas_incidentes.add(todas_as_arestas[chave_aresta].rotulo)
            return arestas_incidentes

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if self.ha_paralelas or self.ha_laco():
            return False

        grau_completo = len(self.vertices) - 1

        for vertice in self.vertices:
            if self.grau(vertice.rotulo) != grau_completo:
                return False

        return True

    def dfs(self, v=''):
        arvoreDfs = MeuGrafo()
        arvoreDfs.adiciona_vertice(v)

        def dfs_recursiva(v, arvoreDfs):
            adjacencia = list(self.arestas_sobre_vertice(v))
            adjacencia = sorted(adjacencia)
            for i in adjacencia:
                a: Aresta = self._arestas[i]
                vertice_seguinte = a.v2 if a.v1.rotulo == v else a.v1
                if not arvoreDfs.existe_rotulo_vertice(vertice_seguinte.rotulo):
                    arvoreDfs.adiciona_vertice(vertice_seguinte.rotulo)
                    arvoreDfs.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
                    print(arvoreDfs)
                    dfs_recursiva(vertice_seguinte.rotulo, arvoreDfs)

            return arvoreDfs
        return dfs_recursiva(v, arvoreDfs)

    def bfs(self, v=''):
        arvoreBfs = MeuGrafo()
        arvoreBfs.adiciona_vertice(v)

        def bfs_recursiva(v, arvoreBfs):
            adjacencia = list(self.arestas_sobre_vertice(v))
            adjacencia = sorted(adjacencia)
            v_adjacentes = []
            for i in adjacencia:
                a: Aresta = self._arestas[i]
                vertice_seguinte = a.v2 if a.v1.rotulo == v else a.v1
                if not arvoreBfs.existe_rotulo_vertice(vertice_seguinte.rotulo):
                    v_adjacentes.append(vertice_seguinte)
                    arvoreBfs.adiciona_vertice(vertice_seguinte.rotulo)
                    arvoreBfs.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
                    print(arvoreBfs)
            for i in v_adjacentes: bfs_recursiva(i.rotulo, arvoreBfs)
            return arvoreBfs
        return bfs_recursiva(v, arvoreBfs)




