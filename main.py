from services.catalogo_service import Catalogo
from services.carrito_service import Carrito
from services.factura_service import Facturacion

def main():
    catalogo = Catalogo()
    carrito = Carrito()
    
    # Carga inicial
    print("--- Sistema de Tienda de Videojuegos LEAD University ---")
    formato_carga = input("¿Cargar catálogo desde 'json' o 'csv'?: ").strip().lower()
    if formato_carga in ['json', 'csv']:
        catalogo.cargar_catalogo(f"data/catalogo.{formato_carga}", formato_carga)
    else:
        print("Formato inválido. Iniciando catálogo vacío.")

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar catálogo")
        print("2. Agregar nuevo videojuego al catálogo")
        print("3. Agregar juego al carrito")
        print("4. Ver carrito y eliminar items")
        print("5. Finalizar compra (Generar Factura)")
        print("6. Guardar catálogo y Salir")
        
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                catalogo.mostrar_catalogo()

            elif opcion == '2':
                print("\n-- Agregar Nuevo Videojuego --")
                id_juego = input("ID único: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = input("Precio: ")
                esrb = input("Clasificación ESRB: ")
                stock = input("Stock: ")
                consola = input("Consola (PS5/Xbox/Nintendo): ")
                
                catalogo.agregar_juego(id_juego, nombre, categoria, precio, esrb, stock, consola)

            elif opcion == '3':
                id_juego = int(input("Ingrese el ID del juego a comprar: "))
                juego = catalogo.buscar_por_id(id_juego)
                if not juego:
                    print("Error: El videojuego no existe.")
                    continue
                cantidad = int(input("Cantidad: "))
                carrito.agregar_item(juego, cantidad)

            elif opcion == '4':
                carrito.mostrar_carrito()
                if carrito.items:
                    eliminar = input("¿Desea eliminar algún juego del carrito? (s/n): ").lower()
                    if eliminar == 's':
                        id_eliminar = int(input("Ingrese el ID del juego a eliminar: "))
                        carrito.eliminar_item(id_eliminar)

            elif opcion == '5':
                if not carrito.items:
                    print("El carrito está vacío.")
                    continue
                carrito.mostrar_carrito()
                cliente = input("\nNombre del cliente: ")
                formato = input("Formato de factura (json/csv): ").lower()
                nombre_archivo = input("Nombre del archivo (sin extensión): ")
                
                Facturacion.generar_factura(cliente, carrito, formato, nombre_archivo)
                print("¡Compra finalizada con éxito!")

            elif opcion == '6':
                formato = input("¿En qué formato desea guardar el catálogo? (json/csv): ").lower()
                if formato in ['json', 'csv']:
                    catalogo.guardar_catalogo(f"data/catalogo_actualizado.{formato}", formato)
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

        # Manejo de Excepciones global para el menú
        except ValueError as ve:
            print(f"Error de validación: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
