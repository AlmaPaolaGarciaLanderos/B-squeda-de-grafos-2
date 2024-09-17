#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial    

import heapq

def dijkstra(grafo, inicio):
    """
    Encuentra el camino más corto desde el nodo 'inicio' a todos los demás nodos usando el algoritmo de Dijkstra.
    :param grafo: Diccionario que representa el grafo ponderado.
    :param inicio: Nodo de inicio.
    :return: Diccionario con las distancias mínimas desde el nodo de inicio a cada nodo.
    """
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]  # (distancia, nodo)

    while cola:
        distancia_actual, nodo = heapq.heappop(cola)
        
        if distancia_actual > distancias[nodo]:
            continue
        
        for vecino, peso in grafo[nodo].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))
    
    return distancias

# Ejemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
inicio = 'A'
distancias = dijkstra(grafo, inicio)
print(f"Distancias desde {inicio}: {distancias}")
