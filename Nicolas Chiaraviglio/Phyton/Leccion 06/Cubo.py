class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidadm con
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
        
    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad
    
ancho = int(input('Escriba el ancho del cubo: '))
alto = int(input('Escriba el alto del cubo: '))
profundidad = int(input('Escriba la profundidad del cubo: '))

cubo1 = Cubo(ancho, alto, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')