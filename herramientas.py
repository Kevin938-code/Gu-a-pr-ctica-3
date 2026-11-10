import os

COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

RESPUESTAS = ("si", "sí", "s", "yes", "y", "Si", "SI", "SÍ", "Sí", "YES", "Y")

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def imprimir_color(texto, color):
    codigo = COLORES.get(color, COLORES["BLANCO"])
    print(f"{codigo}{texto}{COLORES['RESET']}")

def imprimir_titulo(texto):
    borrar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()

def imprimir_exito(mensaje):
    imprimir_color(f"  ✓ {mensaje}", "VERDE")

def imprimir_error(mensaje):
    imprimir_color(f"  ✗ {mensaje}", "ROJO")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")

def es_mayor_de_edad(self):
        return leer_entero(self.edad >= 18)

def menu(titulo, opciones):
    for opcion in opciones:
        print(f" {opcion}")
    return input(f"opción[0...{len(opciones)-1}]:  ").strip().upper()

if __name__ == "__main__":
    opc = menu("Menú principal", ["1) Pila", "2) Cola", "0) salir"])
    opc1 = menu("Menú Pila", ["1) Entrar a la pila", "2) Listar", "3) Desapilar", "4) Cargar datos de prueba", "0) salir"])
    opc2 = menu("Menú Cola", ["1) Entrar a la cola", "2) Listar", "3) Desencolar", "4) Cargar datos de prueba", "0) salir"])
