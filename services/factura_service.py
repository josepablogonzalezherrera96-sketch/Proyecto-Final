from utils.manejador_archivos import escribir_json, escribir_csv
from datetime import datetime

class Facturacion:
    @staticmethod
    def generar_factura(cliente, carrito, formato, nombre_archivo):
        if not carrito.items:
            raise ValueError("No se puede generar una factura de un carrito vacío.")

        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lista_compras = []
        
        for item in carrito.items:
            j = item['juego']
            lista_compras.append({
                "juego_id": j.id,
                "nombre": j.nombre,
                "cantidad": item['cantidad'],
                "precio_unitario": j.precio,
                "subtotal": j.precio * item['cantidad']
            })

        datos_factura = {
            "cliente": cliente,
            "fecha": fecha_actual,
            "detalle": lista_compras,
            "total_pagado": carrito.calcular_total()
        }

        # Descontar stock real del catálogo
        for item in carrito.items:
            item['juego'].stock -= item['cantidad']

        if formato == 'json':
            escribir_json(f"{nombre_archivo}.json", datos_factura)
            print(f"Factura generada: {nombre_archivo}.json")
        elif formato == 'csv':
            # Para CSV aplanamos los datos
            campos = ['cliente', 'fecha', 'juego_id', 'nombre', 'cantidad', 'precio_unitario', 'subtotal', 'total_pagado']
            datos_planos = []
            for d in lista_compras:
                fila = {"cliente": cliente, "fecha": fecha_actual, "total_pagado": datos_factura['total_pagado']}
                fila.update(d)
                datos_planos.append(fila)
            escribir_csv(f"{nombre_archivo}.csv", datos_planos, campos)
            print(f"Factura generada: {nombre_archivo}.csv")
            
        carrito.vaciar()
