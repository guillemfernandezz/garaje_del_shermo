class GeoData:
    def __init__(self, file_name: str, file_size: float):
        self.file_name = file_name
        self.file_size = file_size
        
    def __str__(self):
        return f"|- Nombre: {self.file_name}\n|- Tamaño: {self.file_size} GB "
    
    def publish(self):
        return f"|- Publicando {self.file_name} en el servidor del organismo..."
    
class VectorData(GeoData):
    def __init__(self, file_name: str, file_size: float, geometry_type: str):
        super().__init__(file_name, file_size)
        self.geometry_type = geometry_type
        
    def publish(self):
        mensaje = super().publish()
        return f"{mensaje}\n [LOG] Generando piramides para optimización Windows"
        
class RasterData(GeoData):
    def __init__(self, file_name: str, file_size: float, resolution_m: float):
        super().__init__(file_name, file_size)
        self.resolution_m = resolution_m
        
capa_orto = VectorData("ortofoto_2024.tif", 500.5, "POINT")
print(capa_orto.publish())