from models.videojuego import JuegoPS5, JuegoXbox, JuegoNintendo, VideoJuego
from utils.manejador_archivos import leer_json, leer_csv, escribir_json, escribir_csv

class Catalogo:
    def __init__(self):
        self.juegos = []

    def instanciar_juego(self, datos):
        consola = datos.get('consola', '').upper()
        if consola == 'PS5': return JuegoPS5(**self._filtrar_datos(datos))
        elif consola == 'XBOX': return JuegoXbox(**self._filtrar_datos(datos))
        elif consola == 'NINTENDO': return JuegoNintendo(**self._filtrar_datos(datos))
        else: return VideoJuego(**datos)

    def _filtrar_datos(self, datos):
        return {k: v for k, v in datos.items() if k != 'consola'}

    def cargar_catalogo(self, ruta, formato):
        self.juegos = []
        try:
            if formato == 'json':
                datos = leer_json(ruta)
            elif formato == 'csv':
                datos = leer_csv(ruta)
            
            for d in datos:
                # Convertimos tipos numéricos desde CSV
                d['id'] = int(d['id'])
                d['precio'] = float(d['precio'])
                d['stock'] = int(d['stock'])
                self.juegos.append(self.instanciar_juego(d))
            print(f"Catálogo cargado exitosamente ({len(self.juegos)} juegos).")
        except Exception as e:
            print(f"Error al cargar el catálogo: {e}")

    def buscar_por_id(self, id_juego):
        for juego in self.juegos:
            if juego.id == id_juego:
                return juego
        return None

    def agregar_juego(self, id_juego, nombre, categoria, precio, esrb, stock, consola):
        # Validaciones requeridas
        if not all([str(id_juego), nombre, categoria, str(precio), esrb, str(stock), consola]):
            raise ValueError("No se permiten campos vacíos.")
        if self.buscar_por_id(int(id_juego)):
            raise ValueError("El identificador ya existe.")
        if float(precio) < 0:
            raise ValueError("El precio no puede ser negativo.")
        if int(stock) < 0:
            raise ValueError("El stock no puede ser negativo.")

        datos = {
            "id_juego": int(id_juego), "nombre": nombre, "categoria": categoria,
            "precio": float(precio), "esrb": esrb, "stock": int(stock), "consola": consola.upper()
        }
        
        nuevo_juego = self.instanciar_juego({"consola": consola.upper(), "id": int(id_juego), **datos})
        self.juegos.append(nuevo_juego)
        print("¡Videojuego agregado con éxito!")

    def guardar_catalogo(self, ruta, formato):
        datos = [j.to_dict() for j in self.juegos]
        if formato == 'json':
            escribir_json(ruta, datos)
        elif formato == 'csv':
            campos = ['id', 'nombre', 'categoria', 'precio', 'esrb', 'stock', 'consola']
            escribir_csv(ruta, datos, campos)
        print("Catálogo guardado exitosamente.")

    def mostrar_catalogo(self):
        for juego in self.juegos:
            print(juego)
