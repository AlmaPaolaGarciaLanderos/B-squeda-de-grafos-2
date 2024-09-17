#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

def floyd_warshall(grafo):
    """
    Encuentra el camino más corto entre todos los pares de nodos usando el algoritmo de Floyd-Warshall.
    :param grafo: Diccionario que representa el grafo ponderado.
    :return: Diccionario de diccionarios con las distancias mínimas entre todos los pares de nodos.
    """
    nodos = grafo.keys()
    distancias = {nodo: {vecino: float('infinity') for vecino in nodos} for nodo in nodos}
    
    for nodo in nodos:
        distancias[nodo][nodo] = 0
        for vecino, peso in grafo[nodo].items():
            distancias[nodo][vecino] = peso

    for k in nodos:
        for i in nodos:
            for j in nodos:
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    
    return distancias

# Ejemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
distancias = floyd_warshall(grafo)
print("Matriz de distancias más cortas entre todos los pares de nodos:")
for origen in distancias:
    print(f"{origen}: {distancias[origen]}")
