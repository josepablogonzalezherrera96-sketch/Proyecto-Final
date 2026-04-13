class Carrito:
    def __init__(self):
        self.items = [] # Lista de diccionarios {'juego': objeto, 'cantidad': int}

    def agregar_item(self, juego, cantidad):
        if juego.stock < cantidad:
            raise ValueError(f"Stock insuficiente. Solo hay {juego.stock} disponibles.")
        
        # Verificar si ya está en el carrito
        for item in self.items:
            if item['juego'].id == juego.id:
                if item['juego'].stock < (item['cantidad'] + cantidad):
                    raise ValueError("La cantidad total excede el stock disponible.")
                item['cantidad'] += cantidad
                return
        
        self.items.append({'juego': juego, 'cantidad': cantidad})
        print(f"Agregado: {juego.nombre} x{cantidad}")

    def eliminar_item(self, id_juego):
        self.items = [item for item in self.items if item['juego'].id != id_juego]
        print("Item eliminado del carrito (si existía).")

    def mostrar_carrito(self):
        if not self.items:
            print("El carrito está vacío.")
            return
        print("\n--- Carrito de Compras ---")
        for i, item in enumerate(self.items, 1):
            j = item['juego']
            subtotal = j.precio * item['cantidad']
            print(f"{i}. {j.nombre} - Cantidad: {item['cantidad']} - Subtotal: ${subtotal:.2f}")
        print(f"Total a pagar: ${self.calcular_total():.2f}")

    def calcular_total(self):
        return sum(item['juego'].precio * item['cantidad'] for item in self.items)
        
    def vaciar(self):
        self.items = []
