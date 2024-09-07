from Conversion import Conversion

class Factura:
    def __init__(self, no_factura, fecha, nombre_cliente, telefono, direccion, rfc):
        self.__no_factura = no_factura
        self.__fecha = fecha
        self.__nombre_cliente = nombre_cliente
        self.__telefono = telefono
        self.__direccion = direccion
        self.__rfc = rfc
        self.__productos = []
        self.__subtotal = 0.0
        self.__iva = 0.0
        self.__total = 0.0
        self.__conversion = Conversion()

    # Métodos set y get para los atributos privados
    def set_producto(self, no_producto, nombre, cantidad, precio_unitario):
        importe = cantidad * precio_unitario
        self.__productos.append([no_producto, nombre, cantidad, precio_unitario, importe])

    def get_productos(self):
        return self.__productos

    # Métodos para calcular subtotal, IVA y total
    def calcular_subtotal(self):
        self.__subtotal = sum([producto[4] for producto in self.__productos])

    def calcular_iva(self):
        self.__iva = self.__subtotal * 0.16

    def calcular_total(self):
        self.__total = self.__subtotal + self.__iva

    def get_total(self):
        return self.__total

    # Método para generar la factura en formato de texto
    def generar_factura(self):
        self.calcular_subtotal()
        self.calcular_iva()
        self.calcular_total()

        print(f"Factura No: {self.__no_factura}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__nombre_cliente}")
        print(f"Teléfono: {self.__telefono}")
        print(f"Dirección: {self.__direccion}")
        print(f"RFC: {self.__rfc}")
        print("-" * 50)
        print(f"{'No.':<10}{'Producto':<20}{'Cant.':<10}{'P.Unit':<10}{'Importe'}")
        for producto in self.__productos:
            print(f"{producto[0]:<10}{producto[1]:<20}{producto[2]:<10}{producto[3]:<10}{producto[4]:<10.2f}")
        print("-" * 50)
        print(f"Subtotal: {self.__subtotal:.2f}")
        print(f"IVA (16%): {self.__iva:.2f}")
        print(f"Total: {self.__total:.2f}")
        print(f"Total en letras: {self.__conversion.convertir_numero_con_centavos(self.__total)}")
