import requests
from datetime import datetime
from typing import List, Tuple

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
