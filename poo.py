
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print(f"El coche ha acelerado a {self.velocidad} km/h")

    def frenar(self, velocidad):
        self.velocidad = max(0, self.velocidad - velocidad)
        print(f"El coche ha frenado a {self.velocidad} km/h")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Velocidad actual: {self.velocidad} km/h")



class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes para retirar.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo:.2f}")



class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"Ancho: {self.ancho}")
        print(f"Alto: {self.alto}")
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")


if __name__ == "__main__":

    coche = Coche("Toyota", "Corolla", "Rojo")
    coche.mostrar_info()
    coche.acelerar(50)
    coche.frenar(20)
    coche.mostrar_info()

    print("\n--------------------------\n")

    
    cuenta = CuentaBancaria("Juan Pérez")
    cuenta.mostrar_saldo()
    cuenta.depositar(1000)
    cuenta.retirar(300)
    cuenta.retirar(800)  
    cuenta.mostrar_saldo()

    print("\n--------------------------\n")

    
    rect = Rectangulo(5.0, 3.0)
    rect.mostrar_info()
