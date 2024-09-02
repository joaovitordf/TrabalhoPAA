"""
// Nome(s) Discente(s): João Vitor Dias Fernandes
// Matrícula(s): 0056152
// Data: 02/09/2024

// Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que //foram fornecidas pelo professor foram desenvolvidas por mim. Declaro também que
// sou responsável por todas  as eventuais cópias deste programa e que não distribui nem facilitei a //distribuição de cópias.

Alguns links uteis: 
https://calcworkshop.com/trees-graphs/graph-coloring/
https://youtu.be/Qyv20alPqec?si=FwIqM8EIQFQV01KN
"""

class Grafo:
    def __init__(self):
        self.grafo_dict = {}
        self.cores = {}

    def adiciona_no(self, no):
        if no not in self.grafo_dict:
            self.grafo_dict[no] = []
            self.cores[no] = None

    def adiciona_aresta(self, no1, no2):
        self.grafo_dict[no1].append(no2)
        self.grafo_dict[no2].append(no1)

    def print_grafo(self):
        for no in self.grafo_dict:
            vizinhos = ", ".join(map(str, self.grafo_dict[no]))
            print(f"{no}: {vizinhos}")

    def num_vertices(self):
        return len(self.grafo_dict)
    
    def colore_grafo(self, m):
        if not self.colore_grafo_util(m, list(self.grafo_dict.keys())[0]):
            print("Solucao inexistente")
            return False

        return True
    
    def colore_grafo_util(self, m, v):
        if v is None:
            return True
        
        for c in range(1, m + 1):
            if self.verifica_vizinhos(v, c):
                self.cores[v] = c

                proximo_vertice = self.proximo_vertice(v)

                if self.colore_grafo_util(m, proximo_vertice):
                    return True
                
                self.cores[v] = None
        
        return False
        
        
    def verifica_vizinhos(self, v, c):
        for vizinho in self.grafo_dict[v]:
            if self.cores[vizinho] == c:
                return False
        return True
    
    def proximo_vertice(self, vertice_atual):
        vertices = list(self.grafo_dict.keys())
        atual = vertices.index(vertice_atual)
        if atual < len(vertices) - 1:
            return vertices[atual + 1]
        else:
            return None
        
    def mostra_cores(self):
        for no, cor in self.cores.items():
            print(f"Vértice {no} -> Cor {cor}")
            
    def colore_grafo_guloso(self, m):
        vertices_com_graus = []
        for vertice in self.grafo_dict:
            grau = len(self.grafo_dict[vertice])
            vertices_com_graus.append((vertice, grau))

        vertices_com_graus.sort(reverse=True, key=lambda item: item[1])

        vertices_ordenados = []
        for vertice, _ in vertices_com_graus:
            vertices_ordenados.append(vertice)

        for v in vertices_ordenados:
            for c in range(1, m + 1):
                if self.verifica_vizinhos(v, c):
                    self.cores[v] = c
                    break

        if None in self.cores.values():
            print("Solucao inexistente")
            return False

        return True

def main():
    grafo1 = Grafo()

    grafo1.adiciona_no('A')
    grafo1.adiciona_no('B')
    grafo1.adiciona_no('C')
    grafo1.adiciona_no('D')
    grafo1.adiciona_no('E')
    grafo1.adiciona_no('F')
    grafo1.adiciona_no('G')
    grafo1.adiciona_no('H')

    grafo1.adiciona_aresta('A', 'B')
    grafo1.adiciona_aresta('A', 'C')
    grafo1.adiciona_aresta('B', 'C')
    grafo1.adiciona_aresta('B', 'D')
    grafo1.adiciona_aresta('C', 'D')
    grafo1.adiciona_aresta('C', 'E')
    grafo1.adiciona_aresta('C', 'G')
    grafo1.adiciona_aresta('D', 'E')
    grafo1.adiciona_aresta('E', 'G')
    grafo1.adiciona_aresta('E', 'F')
    
    grafo2 = Grafo()

    grafo2.adiciona_no('A')
    grafo2.adiciona_no('B')
    grafo2.adiciona_no('C')
    grafo2.adiciona_no('D')
    grafo2.adiciona_no('E')
    grafo2.adiciona_no('F')
    grafo2.adiciona_no('G')
    grafo2.adiciona_no('H')

    grafo2.adiciona_aresta('A', 'B')
    grafo2.adiciona_aresta('A', 'C')
    grafo2.adiciona_aresta('B', 'C')
    grafo2.adiciona_aresta('B', 'D')
    grafo2.adiciona_aresta('C', 'D')
    grafo2.adiciona_aresta('C', 'E')
    grafo2.adiciona_aresta('C', 'G')
    grafo2.adiciona_aresta('D', 'E')
    grafo2.adiciona_aresta('E', 'G')
    grafo2.adiciona_aresta('E', 'F')

    # Quantidade de cores
    m = 3
    grafo1.colore_grafo(m)
    grafo1.mostra_cores()
    print("--------------------------------------")
    grafo2.colore_grafo_guloso(m)
    grafo2.mostra_cores()

if __name__ == '__main__':
    main()