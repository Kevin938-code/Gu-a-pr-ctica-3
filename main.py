from herramientas import (
    borrar_pantalla,
    imprimir_error,
    imprimir_exito,
    imprimir_titulo,
    leer_entero,
    menu,
)
from mi_cola import MiCola
from mi_pila import MiPila
from pasajero import Pasajero

pila = MiPila(10)
cola = MiCola(10)
#Funciones de ayuda a mi_cola

def pausa():
    input("\nPresione Enter para continuar...")

def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)
#pas1 = Pasajero(12, "ana", "34443", 34,date(),"cuenca","12A")
#pas = leer_pasajero()
#print(pas)

# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        imprimir_titulo("MENÚ 1 · PILA")
        op = menu("Opciones de Pila", [
            "1) Entrar a la pila", 
            "2) Listar", 
            "3) Desapilar", 
            "4) Ver tope", 
            "5) Buscar pasajeros", 
            "6) Modificar destino/asientos", 
            "7) Eliminar por número", 
            "8) Copiar pila", 
            "9) Longitud", 
            "10) ¿Está vacía?",  
            "C) Cargar datos de prueba", 
            "0) salir"])

        if op == "1":                                  # ✅ ejemplo resuelto
            borrar_pantalla()
            imprimir_titulo("NUEVO PASAJERO EN PILA")
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                imprimir_exito("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
                pausa()
        
        elif op == "2":
            borrar_pantalla()
            imprimir_titulo("LISTADO DE LA PILA")
            pila.listar()
            pausa()
        
        # ✍ TODO: opciones 3 a 9 con el patrón LEER → LLAMAR → MOSTRAR
        
        elif op == "3":
            borrar_pantalla()
            imprimir_titulo("DESAPILAR PASAJERO")
            salido = pila.desapilar()
            if salido:
                tope_actual = pila.ver_tope()
                nuevo_tope_str = tope_actual.nombre if tope_actual else "Ninguno"
                imprimir_exito(f"Salió: {salido.nombre} Nuevo tope: {nuevo_tope_str}")
            else: 
                imprimir_error("La pila está vacía")
                pausa()
    
        elif op == "4":
            borrar_pantalla()
            imprimir_titulo("VER TOPE DE LA PILA")
            tope = pila.ver_tope()
            if tope:
                imprimir_exito(f"Tope actual: {tope}")
            else:
                imprimir_error("La pila está vacía")
            pausa()

        elif op == "5":
            borrar_pantalla()
            imprimir_titulo("BUSCAR PASAJERO EN PILA")
            num = leer_entero("  Número de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                imprimir_exito(f"Encontrado en la posición [{pos}] -> {pila.datos[pos]}")
            else:
                imprimir_error("El pasajero no existe en la pila")
            pausa()
        
        elif op == "6":
            borrar_pantalla()
            imprimir_titulo("MODIFICAR PASAJERO")
            num = leer_entero("  Número de pasajero a modificar: ")
            nuevo_destino = input(" Nuevo destino: ").strip()
            nuevo_asiento = input(" Nuevo asiento: ").strip().upper()
            if pila.modificar(num, nuevo_destino, nuevo_asiento):
                imprimir_exito("Pasajero modificado correctamente")
            else:
                imprimir_error("No se encontró un pasajero con ese número")
            pausa()
        
        elif op == "7":
            borrar_pantalla()
            imprimir_titulo("ELIMINAR PASAJERO POR NÚMERO")
            num = leer_entero("  Número de pasajero a eliminar: ")
            eliminado = pila.eliminar_por_numero(num)
            if eliminado:
                imprimir_exito(f"Pasajero {eliminado.nombre} eliminado exitosamente")
            else:
                imprimir_error("Valor no válido o pasajero no encontrado")
            pausa()

        elif op == "8":
            borrar_pantalla()
            imprimir_titulo("COPIA DE LA PILA")
            pila_copia = pila.copiar()
            imprimir_exito("Copia de la pila creada con éxito. Listando copia:")
            pila_copia.listar()
            pausa()

        elif op == "9":
            borrar_pantalla()
            imprimir_titulo("LONGITUD DE LA PILA")
            print(f"  Longitud de la pila: {pila.longitud()}")
            pausa()
            
        elif op == "10":
            borrar_pantalla()    
            imprimir_titulo("ESTADO DE LA PILA")
            if pila.esta_vacia():
                imprimir_error("La pila está vacía")
            else:
                imprimir_exito("La pila no está vacía")
            pausa()
        
        elif op == "C":
            borrar_pantalla()
            imprimir_titulo("CARGAR DATOS DE PRUEBA")
            for p in datos_prueba():
                pila.apilar(p)
            imprimir_exito("Datos de prueba apilados")
            pausa()
            
        elif op == "0":
            print(" Hasta pronto!")
            break
        else:
            imprimir_error("  Opción no válida")
            pausa()

# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        imprimir_titulo("MENÚ 2 · COLA")
        op = menu("Opciones de Cola", [
            "1) Entrar a la cola", 
            "2) Listar", 
            "3) Desencolar", 
            "4) Ver frente", 
            "5) Buscar pasajeros", 
            "6) Modificar destino/asiento", 
            "7) Eliminar por número", 
            "8) Copiar cola", 
            "9) Longitud",
            "10) Está vacía",
            "11) Ordenar cola (Burbuja)",
            "12) Búsqueda binaria",
            "C) Cargar datos de prueba",
            "0) salir"
            ])

        if op == "1": # ✅ ejemplo resuelto
            borrar_pantalla()
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            borrar_pantalla()
            cola.listar()
            pausa()

        # ✍ TODO: opciones 3 a 9 con el patrón LEER → LLAMAR → MOSTRAR
        
        elif op == "3":
            borrar_pantalla()
            imprimir_titulo("DESENCOLAR PASAJERO")
            salido = cola.desencolar()
            if salido:
                frente_actual = cola.ver_frente()
                nuevo_frente_str = frente_actual.nombre if frente_actual else "Ninguno"
                imprimir_exito(f"Salió: {salido.nombre} · Nuevo frente: {nuevo_frente_str}")
            else:
                imprimir_error("La cola está vacía")
            pausa()

        elif op == "4":
            borrar_pantalla()
            imprimir_titulo("VER FRENTE DE LA COLA")
            frente = cola.ver_frente()
            if frente:
                imprimir_exito(f"Frente actual: {frente}")
            else:
                imprimir_error("La cola está vacía")
            pausa()

        elif op == "5":
            borrar_pantalla()
            imprimir_titulo("BUSCAR PASAJERO EN COLA")
            num = leer_entero("  Número de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                imprimir_exito(f"Encontrado en la posición [{pos}] -> {cola.datos[pos]}")
            else:
                imprimir_error("El pasajero no existe en la cola")
            pausa()

        elif op == "6":
            borrar_pantalla()
            imprimir_titulo("MODIFICAR PASAJERO")
            num = leer_entero("  Número de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(num, nuevo_destino, nuevo_asiento):
                imprimir_exito("Pasajero modificado correctamente")
            else:
                imprimir_error("No se encontró un pasajero con ese número")
            pausa()

        elif op == "7":
            borrar_pantalla()
            imprimir_titulo("ELIMINAR PASAJERO POR NÚMERO")
            num = leer_entero("  Número de pasajero a eliminar: ")
            eliminado = cola.eliminar_por_numero(num)
            if eliminado:
                imprimir_exito(f"Pasajero {eliminado.nombre} eliminado de la cola")
            else:
                imprimir_error("Pasajero no encontrado")
            pausa()

        elif op == "8":
            borrar_pantalla()
            imprimir_titulo("COPIA DE LA COLA")
            cola_copia = cola.copiar()
            imprimir_exito("Copia creada con éxito. Listando copia:")
            cola_copia.listar()
            pausa()

        elif op == "9":
            borrar_pantalla()
            imprimir_titulo("ESTADO DE LA COLA")
            print(f"  Longitud de la cola: {cola.longitud()}")
            pausa()
        
        elif op == "10":
            borrar_pantalla()
            imprimir_titulo("ESTADO DE LA COLA")
            if cola.esta_vacia():
                imprimir_error("La cola está vacía")
            else:
                imprimir_exito("La cola no está vacía")
            pausa()

        elif op == "11":
            borrar_pantalla()
            imprimir_titulo("ORDENAR COLA")
            cola.ordenar()
            imprimir_exito("Cola ordenada por número de pasajero correctamente")
            cola.listar()
            pausa()

        elif op == "12":
            borrar_pantalla()
            imprimir_titulo("BÚSQUEDA BINARIA EN COLA")
            num = leer_entero("  Número de pasajero a buscar por búsqueda binaria: ")
            pos = cola.busqueda_binaria(num)
            if pos != -1:
                imprimir_exito(f"Encontrado mediante búsqueda binaria en la posición [{pos}] -> {cola.datos[pos]}")
            else:
                imprimir_error("No existe (recuerde que la cola debe estar ordenada previamente)")
            pausa()
        
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            imprimir_exito("Datos de prueba encolados")
            pausa()
            
        elif op == "0":
            print(" Hasta pronto!")
            break
        else:
            imprimir_error("  Opción no válida")
            pausa()

# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        imprimir_titulo("MENÚ PRINCIPAL ✅")
        op = menu("Opciones", [
            "1) Pila", 
            "2) Cola", 
            "0) salir"
        ])
        
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. ¡Hasta pronto!")