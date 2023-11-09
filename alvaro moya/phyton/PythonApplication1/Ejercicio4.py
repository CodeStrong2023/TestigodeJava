#Ejercicio Etapas de vida  segun la edad
edad=int(input('Digite su edad: '))
mensaje=None
if 0<= edad < 10: #sintaxis simplificada
    mensaje='la infancia es increible y bella'
elif 10<=edad<20:
    mensaje='tienes muchos cambios, mucho que estudiar'
elif 20<=edad<30:
    mensaje='amor y comienza el trabajo'
elif 30<=edad<40:
    mensaje='comienza a agrandarse la familia'
elif 40<=edad<50:
    mensaje='Disfrutasw de tus hijos'
elif 50<=edad<60:
    mensaje='ya no esperas para poder jubilarte'
elif 60<=edad<70:
    mensaje='te jubilas y viajas'
else:
    mensaje='Error, etapa de vida no reconocida'
print(f'tu edad es: {edad}, {mensaje}')