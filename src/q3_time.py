import json
import re
from collections import Counter
from typing import List, Tuple

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

