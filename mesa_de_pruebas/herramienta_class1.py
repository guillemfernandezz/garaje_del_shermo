class SensorUAV:
    def __init__(self, modelo, resolucion):
        self.modelo = modelo
        self.resolucion = resolucion
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        print(f"Sensor {self.modelo} iniciado.")
        
    def capturar_imagen(self):
        if self.encendido:
            return f"Capturando imagen a {self.resolucion} MP ..."
        else:
            return "Error. El sensor está apagado."
        
class RasterProcessor:
    def __init__(self, path):
        self.path = path
        self.metadata = self._get_metadata() # Método privado para carga inicial

    def _get_metadata(self):
        # Aquí iría lógica con rasterio o GDAL
        return {"driver": "GTiff", "width": 1000, "height": 1000}

    def aplicar_ndvi(self, red_band, nir_band):
        # Lógica de cálculo...
        return "NDVI calculado con éxito."

class Point:
    def __init__(self, x: float, y: float, epsg: int):
        self.x = x
        self.y = y
        self._epsg = epsg                                   # El guion bajo nos indica que es 'privado' (por convención)

    @property
    def epsg(self):
        return self._epsg
    
    @epsg.setter
    def epsg(self, value: int):
        if value < 0:
            raise ValueError("El código EPSG debe ser un número positivo.")
        self._epsg = value
        
class Layer:
    def __init__(self, name: str, source: str):
        self.name = name
        self.source = source
        
    def describe(self):
        return f"Nombre: {self.name}; Source: {self.source}"
    
class VectorLayer(Layer):
    def __init__(self, name, source, geometry_type):
        super().__init__(name, source)
        self.geometry_type = geometry_type
        
    def count_features(self):
        return "Contando unidades vectoriales ..."
    
lyr = VectorLayer("Mike", "ICGC", "Point")

print(lyr.describe())
print(lyr.count_features())

