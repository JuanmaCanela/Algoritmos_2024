class Stack:

    def __init__(self):
        self.__elements = []

    #Apilar
    def push(self, element):
        self.__elements.append(element)

    #Desapilar
    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    #Retorna el elemento de la cima
    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    #Retorna el tamaño de la pila
    def size(self):
        return len(self.__elements)