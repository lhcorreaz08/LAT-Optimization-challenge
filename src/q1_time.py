import json
from collections import defaultdict, Counter
from datetime import datetime
from typing import List, Tuple, Optional


### Q1 Time

### Estratégia: Implementar un algoritmo de map-reduce para el procesamiento de los datos, el cual se encarga de leer el archivo y procesar los datos para obtener el top 10 de usuarios que más tweets han realizado

### Servicios cloud utilizados (GCP): Ninguno

### Mejoras:
### Manejo de librerias como apache spark para el procesamiento de los datos, esto permitiría el uso de spark para el procesamiento de los datos y el uso de un bucket de GCP para el almacenamiento de los archivos.



def map_function(line: str) -> Optional[Tuple[datetime.date, str]]:
    try:
        tweet = json.loads(line)
        fecha = datetime.strptime(tweet['date'][:10], '%Y-%m-%d').date()
        usuario = tweet['user']['username']
        return fecha, usuario
    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON: {e}")
        return None

def reduce_function(mapped_values: List[Tuple[datetime.date, str]]) -> List[Tuple[datetime.date, str]]:
    tweets_por_fecha = defaultdict(list)
    for value in mapped_values:
        if value is not None: 
            fecha, usuario = value
            tweets_por_fecha[fecha].append(usuario)

    usuarios_top_por_fecha = []
    for fecha, usuarios in tweets_por_fecha.items():
        conteo_usuarios = Counter(usuarios)
        usuario_top = conteo_usuarios.most_common(1)[0][0]
        usuarios_top_por_fecha.append((fecha, usuario_top))

    return sorted(usuarios_top_por_fecha, key=lambda x: len(tweets_por_fecha[x[0]]), reverse=True)[:10]

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    mapped_values = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            result = map_function(line)
            if result is not None:
                mapped_values.append(result)

    top_fechas = reduce_function(mapped_values)
    return top_fechas