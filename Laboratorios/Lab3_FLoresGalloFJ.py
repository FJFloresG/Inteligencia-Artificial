class Nodo:
    def __init__(self, dato, hijo = None):
        self.dato = dato
        self.hijo = []
        self.padre = None
        self.dist = None

    def set_hijo(self, hijo):
        self.hijo.append(hijo)

    def get_hijo(self):
        return self.hijo

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_dato(self, dato):
        self.dato = dato

    def get_dato(self):
        return self.dato

    def set_dist(self, dist):
        self.dist = dist

    def get_dist(self):
        return self.dist

    def equal(self, nodo):
        if self.get_dato() == nodo.get_dato():
            return True
        else:
            return False

    def on_lista(self, nodo_lista):
        listed = False
        for n in nodo_lista:
            if self.equal(n):
                listed = True
        return listed

    def __str__(self):
        return str(self.get_dato())

def heuristica(init_nodo, solucion, visitado, num):
    visitado.append(init_nodo.get_dato())
    if init_nodo.get_dato() == solucion:
        return init_nodo
    else:
        for i in range(num-1):
            nodo_dato = init_nodo.get_dato().copy()
            temp = nodo_dato[i]
            nodo_dato[i] = nodo_dato[i+1]
            nodo_dato[i+1] = temp
            new_hijo = Nodo(nodo_dato)
            init_nodo.set_hijo(new_hijo)
            new_hijo.set_padre(init_nodo)

        for hijo_nodo in init_nodo.get_hijo():
            if not hijo_nodo.get_dato() in visitado and improvement(init_nodo, hijo_nodo):
                # Llamada recursiva
                solu = heuristica(hijo_nodo, solucion, visitado, num)
                if solu is not None:
                    return solu
        return None


def improvement(padre_nodo, hijo_nodo):
    padre_quality = 0
    hijo_quality = 0
    padre_dato = padre_nodo.get_dato()
    hijo_dato= hijo_nodo.get_dato()

    for n in range(1, len(padre_dato)):
        if padre_dato[n] > padre_dato[n - 1]:
            padre_quality = padre_quality + 1
        if hijo_dato[n] > hijo_dato[n - 1]:
            hijo_quality = hijo_quality + 1

    if hijo_quality >= padre_quality:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Introduzca la cantidad de digitos a ordenar: "))

    initial_state = list(range(num, 0, -1))
    solucion_state = list(reversed(initial_state))
    visited_nodos = []
    initial_nodo = Nodo(initial_state)
    solucion_nodo = heuristica(initial_nodo, solucion_state, visited_nodos, num)

    result = []
    nodo = solucion_nodo
    while nodo.get_padre() is not None:
        result.append(nodo.get_dato())
        nodo = nodo.get_padre()
    result.append(initial_state)
    result.reverse()
    print(result)

# se Utilizo la Heuristica de Calidad de padre en este caso la capacidad maxima que tiene es de 46 dígitos y el tiempo en el que tarda en responder ,realizar o encontrar la solucion son milesimas.
