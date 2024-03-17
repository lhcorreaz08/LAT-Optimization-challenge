import requests
from datetime import datetime
from typing import List, Tuple

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    url = 'https://q2memory-qmij3rko2a-ue.a.run.app/q2_memory'
    params = {
        "bucket_name": "lat_optimization_challenge",
        "blob_name": "data/q2_memory_farmers-protest-tweets-2021-2-4.json"
    }

    response = requests.post(url, json=params)
    data = response.json()

    result = [(entry["emoji"], entry["count"]) for entry in data]

    return result
