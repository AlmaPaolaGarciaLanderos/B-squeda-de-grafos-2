#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial           

from collections import deque

# Definición del grafo. Cada clave es un usuario y el valor es una lista de amigos.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def buscar_camino_corto(grafo, inicio, fin):
    """
    Encuentra el camino más corto desde el nodo 'inicio' hasta el nodo 'fin' utilizando BFS.
    :param grafo: Diccionario que representa el grafo.
    :param inicio: Nodo de inicio.
    :param fin: Nodo objetivo.
    :return: Lista de nodos que representan el camino más corto.
    """
    # Verificar si el inicio es el mismo que el fin
    if inicio == fin:
        return [inicio]

    # Estructuras para la búsqueda
    cola = deque([inicio])  # Cola para el BFS
    visitados = {inicio: None}  # Diccionario para rastrear los nodos visitados y su predecesor

    while cola:
        nodo_actual = cola.popleft()
        
        # Explorar los vecinos del nodo actual
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados[vecino] = nodo_actual
                if vecino == fin:
                    # Si encontramos el nodo objetivo, reconstruir el camino
                    camino = []
                    while vecino:
                        camino.append(vecino)
                        vecino = visitados[vecino]
                    return camino[::-1]  # Invertir el camino para que esté en el orden correcto
                cola.append(vecino)

    # Si no encontramos el camino
    return None

# Ejemplo de uso
inicio = 'A'
fin = 'F'
camino = buscar_camino_corto(grafo, inicio, fin)
print(f"Camino más corto de {inicio} a {fin}: {camino}")
