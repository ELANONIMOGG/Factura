class Conversion:
    def __init__(self):
        self.unidades = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        self.decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        self.especiales = ["once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
        self.centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def numero_a_letras(self, n):
        def convertir_cientos(n):
            if n == 0:
                return ""
            elif n == 100:
                return "cien"
            else:
                c = n // 100
                d = (n % 100) // 10
                u = n % 10
                resultado = self.centenas[c]
                if d == 1 and u > 0:
                    resultado += " " + self.especiales[u - 1]
                else:
                    resultado += " " + self.decenas[d]
                    if u > 0:
                        resultado += " y " + self.unidades[u] if d > 0 else self.unidades[u]
            return resultado.strip()

        if n == 0:
            return "cero"
        miles = n // 1000
        resto = n % 1000
        resultado = ""
        if miles > 0:
            if miles == 1:
                resultado += "mil"
            else:
                resultado += convertir_cientos(miles) + " mil"
        resultado += " " + convertir_cientos(resto)
        return resultado.strip()

    def convertir_numero_con_centavos(self, numero):
        parte_entera = int(numero)
        centavos = round((numero - parte_entera) * 100)
        texto_parte_entera = self.numero_a_letras(parte_entera)
        if parte_entera == 1:
            texto_parte_entera = "un peso"
        else:
            texto_parte_entera += " pesos"
        if centavos == 0:
            texto_centavos = "00/100"
        else:
            texto_centavos = f"{centavos:02d}/100"
        return f"{texto_parte_entera} {texto_centavos} M.N."
