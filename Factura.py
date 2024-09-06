import Factura.Decimalesp as Decimalesp

def generar_factura():

    print("-" * 30)
    print("Factura")
    print("-" * 30)


    nombre_empresa = input("Nombre de la empresa: ")
    nit = input("Numero de factura: ")
    fecha = input("Fecha (dd/mm/aaaa): ")

    nombre_cliente = input("Nombre del cliente: ")

    productos = []
    while True:
        nombre_producto = input("Nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == "fin":
            break
        cantidad = int(input("Cantidad: "))
        precio_unitario = float(input("Precio unitario: "))
        productos.append((nombre_producto, cantidad, precio_unitario))

    subtotal = 0
    for producto in productos:
        subtotal += producto[1] * producto[2]

    iva = subtotal * 0.16
    total = subtotal + iva

    print("-" * 60)
    print(f"| Nombre de la Empresa:{nombre_empresa}  No factura:{nit}          |")
    print(f"| Fecha: {fecha}    Nombre Cliente: {nombre_cliente}               |")
    print("-" * 60)
    print("| item:    Productos:      cantidad   P.unit   importe     |")
    for producto in productos:
        print(f"|{producto[0]}     {producto[1]}  7 ${producto[2]:.2f}  {producto[1] * producto[2]:.2f}|")
    print("-" * 60)
    print(f"|                                          Subtotal: ${subtotal:.2f}|")
    print(f"|                                         IVA (16%): ${iva:.2f}|")
    print("-" * 60)
    print(f"|                                             Total: ${total:.2f}|")
    print("-" * 60)
    print(convertir_numero_con_centavos(total))

    print("-" * 60)

generar_factura()