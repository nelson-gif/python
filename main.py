def totalPago(pagoSinImpuesto, montoImpuesto):
    return pagoSinImpuesto + pagoSinImpuesto*(montoImpuesto/100)

pago = float(input('Proporcione el pago sin impuesto: '))
impupesto = float(input('proporcione el monto del impuesto: '))

total = totalPago(pago, impupesto)

print(f'El total a pagar es: {total}')

