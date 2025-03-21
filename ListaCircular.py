class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None

    def agregar_estudiante(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        if self.primero is None:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero  # Apunta a sí mismo
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero  # Cierra el círculo

    def mostrar_estudiantes(self):
        if self.primero is None:
            print("No hay estudiantes en la lista.")
            return
        actual = self.primero
        while True:
            print(actual.estudiante)
            actual = actual.siguiente
            if actual == self.primero:
                break

    def eliminar_estudiante(self, estudiante):
        if self.primero is None:
            print("No hay estudiantes en la lista.")
            return

        actual = self.primero
        anterior = None

        while True:
            if actual.estudiante == estudiante:
                if anterior is None:  # Eliminar el primero
                    if actual.siguiente == self.primero:  # Solo hay un nodo
                        self.primero = None
                    else:
                        # Encontrar el último nodo
                        ultimo = self.primero
                        while ultimo.siguiente != self.primero:
                            ultimo = ultimo.siguiente
                        ultimo.siguiente = actual.siguiente
                        self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"Estudiante {estudiante} eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(f"Estudiante {estudiante} no encontrado.")


if __name__ == "__main__":
    lista_estudiantes = ListaCircular()
    lista_estudiantes.agregar_estudiante("Juan Perez")
    lista_estudiantes.agregar_estudiante("Maria Lopez")
    lista_estudiantes.agregar_estudiante("Carlos Garcia")

    print("Lista de estudiantes:")
    lista_estudiantes.mostrar_estudiantes()

    lista_estudiantes.eliminar_estudiante("Maria Lopez")
    print("\nLista de estudiantes despues de eliminar a Maria Lopez:")
    lista_estudiantes.mostrar_estudiantes()