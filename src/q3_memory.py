import requests
from datetime import datetime
from typing import List, Tuple

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
