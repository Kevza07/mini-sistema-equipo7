from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        tarea = Tarea(nombre, descripcion)
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre):
        self.tareas = [t for t in self.tareas if t.nombre != nombre]

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            for tarea in self.tareas:
                print(tarea)

    def completar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.marcar_completada()
                break
