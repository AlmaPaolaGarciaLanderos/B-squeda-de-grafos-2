#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial 


def dfs_tareas(grafo, tarea, visitado=None, orden=None):
    """
    Realiza un recorrido en profundidad (DFS) para obtener el orden de ejecución de las tareas.
    :param grafo: Diccionario que representa las dependencias entre tareas.
    :param tarea: Tarea actual.
    :param visitado: Conjunto de tareas visitadas.
    :param orden: Lista para almacenar el orden de ejecución.
    :return: Orden de ejecución de las tareas.
    """
    if visitado is None:
        visitado = set()
    if orden is None:
        orden = []
    
    visitado.add(tarea)
    for vecino in grafo[tarea]:
        if vecino not in visitado:
            dfs_tareas(grafo, vecino, visitado, orden)
    orden.append(tarea)
    
    return orden

# Ejemplo de uso
grafo = {
    'Tarea1': ['Tarea2', 'Tarea3'],
    'Tarea2': ['Tarea4'],
    'Tarea3': [],
    'Tarea4': []
}
inicio = 'Tarea1'
orden = dfs_tareas(grafo, inicio)
print(f"Orden de ejecución de las tareas: {orden[::-1]}")
