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

        for i in range(6):
            no_producto = entries_productos[i][0].get()
            nombre = entries_productos[i][1].get()
            cantidad = int(entries_productos[i][2].get())
            precio_unitario = float(entries_productos[i][3].get())

            if no_producto and nombre and cantidad > 0 and precio_unitario > 0:
                factura.set_producto(no_producto, nombre, cantidad, precio_unitario)

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

entries_productos = []
for i in range(6):
    row = 7 + i
    tk.Label(root, text=f"Producto {i+1}:").grid(row=row, column=0)
    no_producto = tk.Entry(root)
    no_producto.grid(row=row, column=1)
    nombre_producto = tk.Entry(root)
    nombre_producto.grid(row=row, column=2)
    cantidad_producto = tk.Entry(root)
    cantidad_producto.grid(row=row, column=3)
    precio_unitario_producto = tk.Entry(root)
    precio_unitario_producto.grid(row=row, column=4)
    entries_productos.append([no_producto, nombre_producto, cantidad_producto, precio_unitario_producto])


btn_generar = tk.Button(root, text="Generar Factura", command=generar_factura)
btn_generar.grid(row=13, column=1, columnspan=2)

root.mainloop()
