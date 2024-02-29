class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.next = None
        # se crea el objeto de "término" para cada término que lleve el polinomio


class Polinomio:
    def __init__(self):
        # se crea la "lista" para los términos que conforman el polinomio
        self.head = None
        self.tail = None

    def agregar(self, coeficiente, exponente):  # función para agregar un nuevo término
        new = Nodo(coeficiente, exponente)
        if not self.head:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.tail.next = self.head  # Hacer que el último apunte al primero para formar la lista circular

    def sumar(self, otro_polinomio):
        resultado = Polinomio()
        current1 = self.head
        current2 = otro_polinomio.head
        while True:
            coeficiente1 = current1.coeficiente if current1 else 0
            coeficiente2 = current2.coeficiente if current2 else 0
            exponente1 = current1.exponente if current1 else 0
            exponente2 = current2.exponente if current2 else 0
            nuevo_coeficiente = coeficiente1 + coeficiente2
            nuevo_exponente = max(exponente1, exponente2)
            resultado.agregar(nuevo_coeficiente, nuevo_exponente)
            if current1 == self.tail and current2 == otro_polinomio.ultimo_termino:
                break
            current1 = current1.siguiente if current1 != self.tail else None
            current2 = current2.siguiente if current2 != otro_polinomio.ultimo_termino else None
        return resultado

    def restar(self, otro_polinomio):
        resultado = Polinomio()
        current1 = self.head
        current2 = otro_polinomio.primer_termino
        while True:
            coeficiente1 = current1.coeficiente if current1 else 0
            coeficiente2 = current2.coeficiente if current2 else 0
            exponente1 = current1.exponente if current1 else 0
            exponente2 = current2.exponente if current2 else 0
            nuevo_coeficiente = coeficiente1 - coeficiente2
            nuevo_exponente = max(exponente1, exponente2)
            resultado.agregar(nuevo_coeficiente, nuevo_exponente)
            if current1 == self.tail and current2 == otro_polinomio.tail:
                break
            current1 = current1.next if current1 != self.tail else None
            current2 = current2.next if current2 != otro_polinomio.tail else None
        return resultado

    def mostrar_polinomio(self):
        polinomio_str = ""
        current = self.head
        while True:
            polinomio_str += f"{current.coeficiente}x^{current.exponente} + "
            if current == self.tail:
                break
            current = current.next
        return polinomio_str[:-3]  # Eliminar el último "+"

    def evaluar(self, valor):
        resultado = 0
        current = self.head
        while True:
            resultado += current.coeficiente * (valor ** current.exponente)
            if current == self.tail:
                break
            current = current.next
        return resultado

# Función para ingresar un polinomio desde la consola
def ingresar_polinomio():
    polinomio = Polinomio()
    while True:
        coeficiente = float(input("Ingrese el coeficiente (0 para terminar): "))
        if coeficiente == 0:
            break
        exponente = int(input("Ingrese el exponente: "))
        polinomio.agregar(coeficiente, exponente)
    return polinomio


polinomio_a = Polinomio()
polinomio_b = Polinomio()
while True:
    print("\nMenú principal")
    print("1. Ingresar componentes a un polinomio")
    print("2. Adición y sustracción")
    print("3. Evaluar polinomios")
    print("4. Salir")
    choice = int(input("Ingrese una opción: "))
    if choice == 1:
        polinomio = input("Ingrese el polinomio (A o B): ")
        if polinomio == "a":
            polinomio_a = ingresar_polinomio()
        elif polinomio == "b":
            polinomio_b = ingresar_polinomio()
        else:
            print("ERROR")
    elif choice == 2:
        operacion = input("Seleccione la operación (+ para sumar, - para restar): ")
        if operacion == "+":
            resultado = polinomio_a.sumar(polinomio_b)
            print("Resultado:", polinomio_a.mostrar_polinomio(resultado))
        elif operacion == "-":
            resultado = polinomio_a.restar(polinomio_b)
            print("Resultado:", polinomio_b.mostrar_polinomio(resultado))
        else:
            print("Operación no válida")
    elif choice == 3:
        polinomio = input("Seleccione el polinomio (a o b): ")
        valor = float(input("Ingrese el valor para evaluar el polinomio: "))
        if polinomio == "a":
            resultado = polinomio_a.evaluar(valor)
        elif polinomio == "b":
            resultado = polinomio_b.evaluar(valor)
        else:
            print("Opción no válida")
        print("Resultado:", resultado)
    elif choice == 4:
        print("Saliendo...")
        break
    else:
        print("Opción no válida")


