from Nodo import Nodo

class Pez:  
    def __init__(self, data = None):
        self.data = data
            

    def cambiarValor(self, nodo):
        for i in range(0, len(nodo.get_estado())-1):
            hijo = nodo.get_estado().copy()
            auxi = hijo[i]
            hijo[i] = hijo[i+1]
            hijo[i+1] = auxi
            modelo = Nodo(hijo)
            nodo.set_hijo(modelo)
        return nodo
        
    def heuristica(self, nodo, solucion):
        lista = []
        nodo = nodo.get_estado()
        for i in range(1, len(nodo)): # recorremos todas las alternativas empezando en la posicion 1
            if(nodo[i] == solucion[i]): lista.append(1)
            else: lista.append(0)

        return sum(lista)
        
    def printPezInicial(pez):
        print('Pez Inicial')
        str = ''
        for i in range(0, len(pez)):
            if(i != 0 and i % 3 == 0): 
                print(str)
                str = ''
            str = str + pez[i]
        print(str)

    def printPezFinal(pez):
        print('Pez Final')
        str = ''
        for i in range(len(pez)):
            str = str + pez[i]
            if(i == 3 or i == 7): 
                print(str)
                str = ''
        print(str)
    
  
    def dfs(self, nodo_inicial, nodo_solucion, visitado):
        visitado.append(nodo_inicial.get_estado())
        if nodo_inicial.get_estado() == nodo_solucion:
            return nodo_inicial
        else:
            nodo_inicial = self.cambiarValor(nodo_inicial)

            for nodo_hijo in nodo_inicial.get_hijo():
                res = self.heuristica(nodo_inicial, nodo_solucion)
      
                if not nodo_hijo.get_estado() in visitado and res >= 5: 
                    Solution = self.dfs(nodo_hijo, nodo_solucion, visitado)
                    if Solution is not None:
                        return Solution
            return None

if __name__ == "__main__":    
    estado_inicial = [
        ' ', '\\', ' ',
        '\\', '/', '\\',
        '/', '\\', '/',
        ' ', '/', ' '
    ]
    Pez.printPezInicial(estado_inicial)
    estado_objetivo = [
        ' ', '/', '\\', ' ',
        '/', '\\', '/', '\\',
        ' ', '/', '\\', ' '
    ]
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = Pez().dfs(nodo_inicial, estado_objetivo, [])

    # Resultado
    result = []
    while nodo_actual.get_padre() is not None:
        result.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    result.append(estado_inicial)
    result.reverse()
    print(result)
    Pez.printPezFinal(result[len(result)-1])
    