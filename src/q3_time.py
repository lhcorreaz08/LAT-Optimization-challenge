import json
import re
from collections import Counter
from typing import List, Tuple

### Q3 Time

### Estratégia: Implementar un algoritmo de map-reduce para el procesamiento de los datos, el cual se encarga de leer el archivo y procesar los datos para obtener el top 10 de usuarios más mencionados en los tweets

### Servicios cloud utilizados (GCP): Ninguno

### Mejoras:
### Manejo de librerias como apache spark para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y el uso de un bucket de GCP para el almacenamiento de los archivos.

def map_mentions(file_path: str) -> List[Tuple[str, int]]:
    user_mentions_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for linea in file:
            try:
                tweet = json.loads(linea)
                user_mentions = re.findall(r'@(\w+)', tweet['content'])
                user_mentions_counter.update(user_mentions)
            except json.JSONDecodeError as e:
                print(f"Error decodificando JSON: {e}")

    return user_mentions_counter.items()

def reduce_mentions(mapped_mentions: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    # Reducir los recuentos sumando los valores para cada usuario
    user_mentions_counter = Counter()
    for user, count in mapped_mentions:
        user_mentions_counter[user] += count

    # Obtener los top 10 usuarios más mencionados
    top_user_mentions = user_mentions_counter.most_common(10)

    return top_user_mentions

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mapped_mentions = map_mentions(file_path)
    top_user_mentions = reduce_mentions(mapped_mentions)

    # Adaptar la estructura de salida
    adapted_output = [(user, count) for user, count in top_user_mentions]

    return adapted_output

