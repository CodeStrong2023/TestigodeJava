# Ejercicio 4: Calculadora de impuestos

#Creamos funcion que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

#Ejecutamos la funcion
pago_sin_impuesto = float(input('Escriba el pago sin impuestos: '))
impuesto = float(input('Escriba el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuestos es: {pago_con_impuesto}')