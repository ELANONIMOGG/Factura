import tkinter as tk
from tkinter import messagebox
from Factura import Factura

def generar_factura():
    try:
        no_factura = entry_factura.get()
        fecha = entry_fecha.get()
        nombre_cliente = entry_cliente.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        rfc = entry_rfc.get()

        factura = Factura(no_factura, fecha, nombre_cliente, telefono, direccion, rfc)

        for i, producto_entries in enumerate(entries_productos):
            nombre = producto_entries[0].get()
            cantidad = int(producto_entries[1].get())
            precio_unitario = float(producto_entries[2].get())
            importe = cantidad * precio_unitario

            if nombre and cantidad > 0 and precio_unitario > 0:
                factura.set_producto(i + 1, nombre, cantidad, precio_unitario)

        factura.generar_factura()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

root = tk.Tk()
root.title("Sistema de Facturación")

tk.Label(root, text="Factura No:").grid(row=0, column=0)
entry_factura = tk.Entry(root)
entry_factura.grid(row=0, column=1)

tk.Label(root, text="Fecha:").grid(row=1, column=0)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=1, column=1)

tk.Label(root, text="Cliente:").grid(row=2, column=0)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=2, column=1)

tk.Label(root, text="Teléfono:").grid(row=3, column=0)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=3, column=1)

tk.Label(root, text="Dirección:").grid(row=4, column=0)
entry_direccion = tk.Entry(root)
entry_direccion.grid(row=4, column=1)

tk.Label(root, text="RFC:").grid(row=5, column=0)
entry_rfc = tk.Entry(root)
entry_rfc.grid(row=5, column=1)

# Etiquetas para productos
tk.Label(root, text="No.").grid(row=6, column=0)
tk.Label(root, text="Producto").grid(row=6, column=1)
tk.Label(root, text="Cantidad").grid(row=6, column=2)
tk.Label(root, text="P.Unitario").grid(row=6, column=3)
tk.Label(root, text="Importe").grid(row=6, column=4)

entries_productos = []
for i in range(6):
    row = 7 + i
    tk.Label(root, text=str(i+1)).grid(row=row, column=0)  # Genera el número de producto automáticamente
    nombre_producto = tk.Entry(root)
    nombre_producto.grid(row=row, column=1)
    cantidad_producto = tk.Entry(root)
    cantidad_producto.grid(row=row, column=2)
    precio_unitario_producto = tk.Entry(root)
    precio_unitario_producto.grid(row=row, column=3)
    importe_label = tk.Label(root, text="0.00")
    importe_label.grid(row=row, column=4)
    entries_productos.append([nombre_producto, cantidad_producto, precio_unitario_producto, importe_label])

btn_generar = tk.Button(root, text="Generar Factura", command=generar_factura)
btn_generar.grid(row=13, column=1, columnspan=2)

root.mainloop()
