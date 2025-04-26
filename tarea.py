# Kevin González Gutiérrez.
# Rama A.
# Tecnologías Computacionales II.
# 26-04-25.

class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

    def __str__(self):
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nCompletada: {self.completada}"
