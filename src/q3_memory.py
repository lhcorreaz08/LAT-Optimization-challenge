import requests
from datetime import datetime
from typing import List, Tuple


### Q3 Memory

### Estratégia: Delegar el procesamiento de los datos a un microservicio de cloud run de (GCP) asi mismo el almacenamiento del archivo se hace mediante un bucket de GCP. Esto permite enviar unicamente el
### request con los datos del archivo a procesar y el contenedor de lo aloja.

### Servicios cloud utilizados (GCP): Cloud Run, Cloud Storage y container registry.

### La lógica del microservicio se encuentra en el directorio ./Cloud Run/Q3_memory_cloud_run con el uso de flask, la implementación algorithm de map-reduce y el archivo dockerfile para la creación de la imagen.

### Mejoras:
### La implementación se puede hacer con un cluster de dataproc para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y
# el uso de un bucket de GCP para el almacenamiento de los archivos.



def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    url = 'https://q3memory-qmij3rko2a-ue.a.run.app/q3_time'
    params = {
        "bucket_name": "lat_optimization_challenge",
        "blob_name": "data/q3_memory_farmers-protest-tweets-2021-2-4.json"
    }

    response = requests.post(url, json=params)
    data = response.json()

    # Modificar la estructura de salida para que coincida con el formato requerido
    result = [(entry[0], entry[1]) for entry in data]

    return result
