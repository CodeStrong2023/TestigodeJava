class Persona2:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self.nombre} {self.apellido} {self.edad}')
        
    @property #Decorador    
    def nombre(self): #Metodo Getter
        print('Estamos utilizando el metodo get')
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre
        
    @property #Decorador    
    def apellido(self): #Metodo Getter
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido): #Metodo Setter
        self._apellido = apellido
        
        
    @property #Decorador    
    def edad(self): #Metodo Getter
        return self._edad
    
    @edad.setter
    def edad(self, edad): #Metodo Setter
        self._edad = edad
        
    def __del__(self):
        print(f'Persona2: {self.nombre} {self.apellido} {self.edad}')
        
if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre) # Llamamos al metodo getter
    persona1.nombre = 'Juan Pedro' #Llamamos al metodo setter
    print(persona1.nombre) #llamamos al metodo getter
    print(persona1.mostrar_detalles())  #Llamamos metodo mostrar detalles

    print(persona1.edad)

    # Tarea crear tres objetos mas utilizando los metodos getter and setter
    # para modificar los cambios y mostrar

    #Objeto numero 1
    persona2 = Persona2('Maxi', 'Echegaray', 23)
    persona2.nombre = 'David'
    persona2.apellido = 'Beckham'
    persona2.edad = 43
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())

    #Objero numero 2
    persona3 = Persona2('Caro', 'Felisa', 21)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 7
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    #Objeto numero 3
    persona4 = Persona2('Naty', 'Lucer', 35)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 33
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    print(__name__)