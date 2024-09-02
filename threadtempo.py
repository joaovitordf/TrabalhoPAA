import random
import time
import threading

def gera_grafo_aleatorio(self, quantidade_vertices):
    for i in range(1, quantidade_vertices + 1):
        self.adiciona_no(i)
    
    # Gera todas as arestas possíveis
    arestas_possiveis = []
    for i in range(1, quantidade_vertices + 1):
        for j in range(i + 1, quantidade_vertices + 1):
            arestas_possiveis.append((i, j))
    
    # Embaralha as arestas
    random.shuffle(arestas_possiveis)
    
    # Seleciona um número aleatório de arestas
    num_arestas = random.randint(0, len(arestas_possiveis))
    arestas_selecionadas = arestas_possiveis[:num_arestas]
    
    # Adiciona as arestas selecionadas ao grafo
    for (node1, node2) in arestas_selecionadas:
        self.adiciona_aresta(node1, node2)
                    
def testa_tamanho_maximo(self, max_cores, stop_event):
    resultados = {}
    max_instancia = 0
    start_time = time.time()

    while not stop_event.is_set():
        # ---------------------- PROCESSOS ----------------------
        for n in range(1, 50):
            if stop_event.is_set():
                print("Tempo máximo atingido. Interrompendo execução.")
                resultados[time.time() - start_time] = max_instancia
                return resultados 
            self.gera_grafo_aleatorio(n)
            try:
                if self.colore_grafo(max_cores):
                    max_instancia = n
            except:
                break
        # --------------------------------------------
        elapsed_time = time.time() - start_time
        
    print(f"{int(elapsed_time)} segundos se passaram.")
    print(max_instancia)
    resultados[elapsed_time] = max_instancia
    return resultados
    
def cronometro(tempos, stop_event):
    maior_tempo = max(tempos)
    tempos_set = set(tempos)

    for i in range(maior_tempo, 0, -1):
        if stop_event.is_set():
            return
        print(f"Tempo restante: {i} segundos")
        if i in tempos_set:
            print(f"Atingiu o tempo configurado: {i} segundos")
        time.sleep(1)
    
    print("Tempo máximo atingido. Interrompendo execução.")
    stop_event.set()