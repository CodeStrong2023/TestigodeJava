class Rectangulo:
    """
    Crear una clase llamada rectangulo, debe tener 2 atributos: Altura y Base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por 
    el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    def calcular_area(self):
        return self.altura * self.base
    
base = int(input('Escriba el nuemro para la base del rectangulo: '))
altura = int(input('escriba el numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
