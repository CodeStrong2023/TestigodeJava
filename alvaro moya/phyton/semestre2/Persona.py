class Persona: # Creamos una clase
    
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        
    def mostrar_detalle(self): #self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, La direccion es: {self.args}, los datos importantes son {self.kwargs}')
        
       
persona1 = Persona('Ariel', 'Betancud', 32456987, 40)    #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')
persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es :{persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es :{persona1.edad}')

#Atributos son: caracteristicas
#Metodos son : el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle() # la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle() #Debemos pasarle una referencia para el self o dará error
persona1.telefono = '44445555289'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}') #Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo y da error
persona3 = Persona('Rogelio','Romero', 35789456, 22, 'Telefono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021) 
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar(esta encapsulado), esto dice que lo desconocemos
#persona3.__nombre #Esta totalmente encapsulado