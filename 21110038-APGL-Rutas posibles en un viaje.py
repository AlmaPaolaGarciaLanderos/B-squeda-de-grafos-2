#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial  

from collections import deque

def bfs_rutas(grafo, inicio, fin):
    """
    Encuentra todas las rutas posibles desde el nodo 'inicio' hasta el nodo 'fin' usando BFS.
    :param grafo: Diccionario que representa el grafo.
    :param inicio: Nodo de inicio.
    :param fin: Nodo objetivo.
    :return: Lista de rutas posibles.
    """
    rutas = []
    cola = deque([(inicio, [inicio])])  # (nodo actual, ruta actual)

    while cola:
        nodo_actual, ruta_actual = cola.popleft()
        if nodo_actual == fin:
            rutas.append(ruta_actual)
        else:
            for vecino in grafo[nodo_actual]:
                if vecino not in ruta_actual:
                    cola.append((vecino, ruta_actual + [vecino]))
    
    return rutas

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
fin = 'F'
rutas = bfs_rutas(grafo, inicio, fin)
print(f"Rutas desde {inicio} a {fin}: {rutas}")
