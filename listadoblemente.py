#Giusseppe Marinelly y Arvelo
class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_estudiante(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        if self.primero is None:  # Si la lista está vacía
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def mostrar_estudiantes(self):
        if self.primero is None:
            print("No hay estudiantes en la lista.")
            return
        actual = self.primero
        while actual:
            print(actual.estudiante)
            actual = actual.siguiente

    def eliminar_estudiante(self, estudiante):
        if self.primero is None:
            print("No hay estudiantes en la lista.")
            return

        actual = self.primero

        while actual:
            if actual.estudiante == estudiante:
                if actual.anterior:  # Si no es el primer nodo
                    actual.anterior.siguiente = actual.siguiente
                else:  # Si es el primer nodo
                    self.primero = actual.siguiente

                if actual.siguiente:  # Si no es el último nodo
                    actual.siguiente.anterior = actual.anterior
                else:  # Si es el último nodo
                    self.ultimo = actual.anterior

                print(f"Estudiante {estudiante} eliminado.")
                return
            actual = actual.siguiente
        print(f"Estudiante {estudiante} no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    lista_estudiantes = ListaDobleEnlazada()
    lista_estudiantes.agregar_estudiante("Juan Perez")
    lista_estudiantes.agregar_estudiante("Maria Lopez")
    lista_estudiantes.agregar_estudiante("Carlos Garcia")

    print("Lista de estudiantes:")
    lista_estudiantes.mostrar_estudiantes()

    lista_estudiantes.eliminar_estudiante("Maria Lopez")
    print("\nLista de estudiantes despues de eliminar a Maria Lopez:")
    lista_estudiantes.mostrar_estudiantes()