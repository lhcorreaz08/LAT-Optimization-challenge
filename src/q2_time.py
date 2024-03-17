import emoji
import json
from collections import Counter
from typing import List, Tuple

### Q2 Time

### Estratégia: Implementar un algoritmo de map-reduce para el procesamiento de los datos, el cual se encarga de leer el archivo y procesar los datos para obtener el top 10 de emojis más utilizados en los tweets

### Servicios cloud utilizados (GCP): Ninguno

### Mejoras:
### Manejo de librerias como apache spark para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y el uso de un bucket de GCP para el almacenamiento de los archivos.



# Función Map: Procesa cada línea (tweet) para encontrar emojis
def map_function(line):
    try:
        tweet = json.loads(line)
        emojis_found = emoji.emoji_list(tweet['content'])
        return [item['emoji'] for item in emojis_found]
    except json.JSONDecodeError:
        return []

# Función Shuffle: Organiza los emojis encontrados para su procesamiento en el Reduce
def shuffle_and_sort(mapped_values):
    all_emojis = []
    for emoji_list in mapped_values:
        all_emojis.extend(emoji_list)
    return Counter(all_emojis)

# Función Reduce: Agrega los conteos de cada emoji
def reduce_function(shuffled_data):
    return shuffled_data.most_common(10)

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    mapped_values = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            mapped_values.extend(map_function(line))

    shuffled_data = shuffle_and_sort(mapped_values)
    reduced_data = reduce_function(shuffled_data)

    return reduced_data