class VideoJuego:
    def __init__(self, id_juego, nombre, categoria, precio, esrb, stock, consola):
        self._id = id_juego
        self._nombre = nombre
        self._categoria = categoria
        self._precio = float(precio)
        self._esrb = esrb
        self._stock = int(stock)
        self._consola = consola

    # Encapsulamiento con @property
    @property
    def id(self): return self._id

    @property
    def nombre(self): return self._nombre

    @property
    def precio(self): return self._precio

    @property
    def stock(self): return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    @property
    def consola(self): return self._consola

    def to_dict(self):
        return {
            "id": self._id, "nombre": self._nombre, "categoria": self._categoria,
            "precio": self._precio, "esrb": self._esrb, "stock": self._stock, "consola": self._consola
        }

    # Polimorfismo
    def __str__(self):
        return f"[{self._id}] {self._nombre} ({self._consola}) - ${self._precio} | Stock: {self._stock}"

# Clases Hijas
class JuegoPS5(VideoJuego):
    def __init__(self, id_juego, nombre, categoria, precio, esrb, stock):
        super().__init__(id_juego, nombre, categoria, precio, esrb, stock, "PS5")

class JuegoXbox(VideoJuego):
    def __init__(self, id_juego, nombre, categoria, precio, esrb, stock):
        super().__init__(id_juego, nombre, categoria, precio, esrb, stock, "XBOX")

class JuegoNintendo(VideoJuego):
    def __init__(self, id_juego, nombre, categoria, precio, esrb, stock):
        super().__init__(id_juego, nombre, categoria, precio, esrb, stock, "Nintendo")
