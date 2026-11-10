from herramientas import imprimir_error
from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
    sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            imprimir_error("  ⚠ La pila está llena")
            return False
        
        if self.buscar(pasajero.numero) != -1:
            imprimir_error("  ⚠ El número de pasajero ya existe")
            return False
        
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            imprimir_error("  (pila vacía)")
            return
        
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            return None
        
        valor = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return valor

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad-1]

    def buscar(self, numero):
        for i in range(self.cantidad-1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        aux = MiPila(self.capacidad)
        encontrado = None

        while self.cantidad > 0:
            pasajero = self.datos[self.cantidad - 1]
            self.datos[self.cantidad - 1] = None
            self.cantidad = self.cantidad - 1

            if pasajero.numero == numero:
                encontrado = pasajero
                break
            else:
                aux.apilar(pasajero)

        while aux.cantidad > 0:
            pasajero_aux = aux.datos[aux.cantidad - 1]
            aux.datos[aux.cantidad - 1] = None
            aux.cantidad = aux.cantidad - 1

            self.datos[self.cantidad] = pasajero_aux
            self.cantidad = self.cantidad + 1
        return encontrado

    def copiar(self):
        nuevo = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nuevo.apilar(self.datos[i])
        return nuevo

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        if self.cantidad == 0:
            print("lista vacía")
            return True
        return False

if __name__ == "__main__":
    pila = MiPila()
    pila.apilar(Pasajero(1000,"Diana", "0923456789", 22 , "2026-11-15", "Quito",  "12A"))
    pila.apilar(Pasajero(1001, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    pila.apilar(Pasajero(1002, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    pila.listar()
    
    tope = pila.ver_tope()
    print(f"Tope actual: {tope}")
    
    pos_1 = pila.buscar(1002)
    print(f"Buscar 1002 (Ana) -> Posición: {pos_1}")
    pos_2 = pila.buscar(9999)
    print(f"Buscar 9999 (No existe) -> Posición: {pos_2}")
    
    pila.modificar(1002, "Esmeraldas", "04C")
    pila.listar()
    
    eliminado = pila.eliminar_por_numero(1001)
    print(f"Se eliminó a: {eliminado.nombre if eliminado else 'Nadie'}")
    pila.listar()
    
    pila_copia = pila.copiar()
    print("Listando la pila COPIA:")
    pila_copia.listar()
    
    print(f"Longitud de la pila: {pila.longitud()}")
    pila.esta_vacia()
    
    while not pila.esta_vacia():
        saliente = pila.desapilar()
        print(f"Salió: {saliente.nombre} | Nuevo tope: {pila.ver_tope() if pila.ver_tope() else 'Ninguno'}")
        
        print("Intentando ver si está vacía cuando ya no tiene elementos:")
    pila.esta_vacia()