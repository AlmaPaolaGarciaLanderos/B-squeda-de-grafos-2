#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial 

def dfs(grafo, nodo, visitado=None):
    """
    Realiza una búsqueda en profundidad (DFS) en el grafo.
    :param grafo: Diccionario que representa el grafo.
    :param nodo: Nodo actual.
    :param visitado: Conjunto de nodos visitados.
    :return: Lista de nodos visitados.
    """
    if visitado is None:
        visitado = set()
    
    visitado.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)
    
    return list(visitado)

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
inicio = 'A'
visitados = dfs(grafo, inicio)
print(f"Nodos visitados a partir de {inicio}: {visitados}")
