class UAVMission:
    def __init__(self, id_mission: str, altura_vuelo: float, camara_px_width: int):
        self.id_mission = id_mission
        # Usamos el setter para validar incluso en el momento de creación
        self.altura_vuelo = altura_vuelo 
        self.camara_px_width = camara_px_width
        
    @classmethod
    def from_dict(cls, data: dict):
        """
        Toma un diccionario y devuelve una instancia de UAVMission. 
        'cls hace referencia a la clase UAVMission
        """        
        id_m = data.get("id","Sin ID")
        alt = data.get("alt", 0.0)
        px = data.get("sensor_px", 0)
        
        return cls(id_mission = id_m, altura_vuelo = alt, camara_px_width = px)
        
    @property
    def altura_vuelo(self) -> float:
        return self._altura_vuelo
    
    @altura_vuelo.setter
    def altura_vuelo(self, value: float):
        if value <= 0:
            raise ValueError("Error: La altura de vuelo debe ser mayor a 0 metros.")
        self._altura_vuelo = value

    def calculate_gsd(self, sensor_width_mm: float, focal_length_mm: float) -> float:
        """
        Calcula el GSD en cm/pixel.
        """
        gsd = (self.altura_vuelo * sensor_width_mm) / (focal_length_mm * self.camara_px_width)
        return round(gsd * 100, 2) # Devolvemos el valor en cm redondeado

    # MÉTODOS MÁGICOS (Dunder Methods)
    def __str__(self):
        """Lo que ve el usuario final al hacer print(objeto)"""
        return f"Misión UAV '{self.id_mission}' a {self.altura_vuelo}m de altura."

    def __repr__(self):
        """Lo que ve un desarrollador en consola o logs"""
        return f"UAVMission(id='{self.id_mission}', alt={self.altura_vuelo})"
    
datos_api = {
    "id": "BCN_2025_01",
    "alt": 100.5,
    "sensor_px": 9000
}

mision_nueva = UAVMission.from_dict(datos_api)
print(f"Misión cargada: {mision_nueva.id_mission} a {mision_nueva.altura_vuelo}m")