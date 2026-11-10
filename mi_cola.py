from herramientas import imprimir_error
from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
    sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            imprimir_error("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.cantidad == 0:
            return None
        
        valor = self.datos[0]
        for i in range(self.cantidad -1):
            self.datos[i] = self.datos[i+1]
            self.datos[self.cantidad -1] = None
            self.cantidad = self.cantidad - 1
            return valor

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
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
        vueltas = self.cantidad
        encontrado = None

        for _ in range(vueltas):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                encontrado = pasajero
            else:
                self.encolar(pasajero)
        return encontrado

    def copiar(self):
        nueva_cola = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])
        return nueva_cola

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        if self.cantidad == 0:
            print("lista vacía")
            return True
        return False

    def ordenar(self):
        if self.cantidad <= 1:
            return
        
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def busqueda_binaria(self, numero):
        izq = 0
        der = self.cantidad -1
        while izq <= der:
            medio = (izq + der)//2
            if self.datos[medio].numero == numero:
                return medio
            if self.datos[medio].numero < numero:
                izq = medio + 1
            else:
                der = medio - 1 
            return - 1

    def burbuja(self):
        pass



if __name__ == "__main__":
    cola = MiCola()
    cola.encolar(Pasajero("Diana", "0923456789", 22))
    cola.encolar(Pasajero("Ana",   "0912345678", 28))
    cola.encolar(Pasajero("Luis",  "0987654321", 35))
    print(cola.buscar("0987654321"))   # debe imprimir 2
    cola.listar()