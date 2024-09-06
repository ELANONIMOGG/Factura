# Sistema de Facturación

Este es un programa simple de facturación en Python que permite generar facturas para productos, calcular el subtotal, IVA, total, y mostrar el total en palabras utilizando la función `convertir_numero_con_centavos()`.

## Descripción

El programa permite a los usuarios:
- Ingresar los datos de una empresa (nombre, número de factura, fecha).
- Registrar el nombre del cliente.
- Añadir múltiples productos a la factura, con su cantidad y precio unitario.
- Calcular automáticamente el subtotal, IVA (16%) y total.
- Convertir el monto total en palabras, incluyendo centavos, usando la función `convertir_numero_con_centavos()`.

### Ejemplo de Uso

1. El usuario ingresa los detalles de la factura, incluyendo los productos.
2. El sistema genera y muestra una factura detallada con el subtotal, el IVA, el total y el monto total en palabras.



### Generación de Factura

El archivo principal del programa es `Factura.py`, que incluye la función `generar_factura()` encargada de manejar toda la lógica del sistema de facturación. 

Dentro de esta función:

- Se solicita al usuario que ingrese el nombre de la empresa, el número de factura, la fecha y el nombre del cliente.
- Luego, el usuario puede ingresar múltiples productos, cada uno con una cantidad y un precio unitario.
- El sistema calcula:
  - **Subtotal**: La suma del precio de todos los productos.
  - **IVA**: 16% del subtotal.
  - **Total**: Subtotal + IVA.
- El total se convierte a palabras utilizando la función `convertir_numero_con_centavos()` que se encuentra en el módulo `Decimalesp`.

### Convertir Número a Letras

El módulo `Decimalesp` contiene la función `convertir_numero_con_centavos()` que convierte el total en palabras. Esta función:

1. Convierte la parte entera del número (en pesos) en letras.
2. Añade los centavos al final, representados en formato numérico (por ejemplo, "50/100").

### Ejemplo de Factura Generada
```bash
------------------------------
Factura
------------------------------
Nombre de la Empresa: ABC Corp.   No factura: 12345
Fecha: 01/01/2024    Nombre Cliente: Juan Pérez
------------------------------------------------------------
| item:    Productos:      cantidad   P.unit   importe     |
|Producto1     3              1       $10.00    $30.00     |
|Producto2     1              1       $20.00    $20.00     |
------------------------------------------------------------
|                                          Subtotal: $50.00|
|                                          IVA (16%): $8.00|
------------------------------------------------------------
|                                             Total: $58.00|
------------------------------------------------------------
Cincuenta y ocho pesos 00/100 M.N.
------------------------------------------------------------
```

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio en tu máquina local.

   ```bash
   git clone https://github.com/ELANONIMOGG/Factura.git
   cd Factura

## Estructura del Proyecto
  ```bash
  ├── Factura.py
  ├── Factura/
  │   └── Decimalesp.py
  ├── README.md
  └── requirements.txt
  ```

- Factura.py: Archivo principal que genera la factura.
- Factura/Decimalesp.py: Contiene la función convertir_numero_con_centavos() que convierte los montos numéricos a letras.
- README.md: Archivo que contiene la descripción del proyecto.
- requirements.txt: Archivo opcional para instalar dependencias.


## Contribucciones 
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -m 'Añadí nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.
