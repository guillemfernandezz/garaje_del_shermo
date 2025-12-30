import pathlib
import datetime

nombre_file = pathlib.Path(__file__).stem
ruta_file = nombre = pathlib.Path(__file__).parent
tiempo = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
ruta_log = ruta_file / "logs"

if not ruta_log.exists():
    ruta_log.mkdir()
    print("Carpeta logs creada con éxito")
else:
    print("La carpeta logs ya existe")