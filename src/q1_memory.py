import requests
from datetime import datetime
from typing import List, Tuple

### Q1 Memory

### Estratégia: Delegar el procesamiento de los datos a un microservicio de cloud run de (GCP) asi mismo el almacenamiento del archivo se hace mediante un bucket de GCP. Esto permite enviar unicamente el 
### request con los datos del archivo a procesar y el contenedor de lo aloja.

### Servicios cloud utilizados (GCP): Cloud Run, Cloud Storage y container registry. 

### La lógica del microservicio se encuentra en el directorio ./Cloud Run/Q1_memory_cloud_run con el uso de flask, la implementación algorithm de map-reduce y el archivo dockerfile para la creación de la imagen.

### Mejoras:
### La implementación se puede hacer con un cluster de dataproc para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y 
# el uso de un bucket de GCP para el almacenamiento de los archivos.


  

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    url = 'https://q1memory-qmij3rko2a-ue.a.run.app/q1_memory'
    params = {
        "bucket_name": "lat_optimization_challenge",
        "blob_name": "data/q1_memory_farmers-protest-tweets-2021-2-4.json"
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        results_raw = response.json()
        results = [(datetime.strptime(date_str, '%Y-%m-%d').date(), username) for date_str, username in results_raw]
        return results
    else:
        print(f"Error: {response.status_code}")
        return []