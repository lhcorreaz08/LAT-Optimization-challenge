##############################################
########Consumo y uso del microservicio#######
##############################################

def q1_memory() -> List[Tuple[datetime.date, str]]:
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

##############################################
########Implementación del microservicio######
##############################################

from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import storage
from datetime import datetime
from collections import defaultdict, Counter
import json
from typing import List, Tuple, Optional
import os

app = Flask(__name__)
CORS(app)

# Configurar el cliente de Google Cloud Storage
storage_client = storage.Client()

# Get the environment variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/q1_memory', methods=['POST'])
def q1_memory_endpoint():
    # El nombre del bucket y el archivo serán recibidos en el cuerpo de la solicitud
    request_data = request.get_json()
    bucket_name = request_data['bucket_name']
    blob_name = request_data['blob_name']
    
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Descargar el contenido del archivo en forma de texto
        content = blob.download_as_text()
        lines = content.split('\n')
        
        mapped_values = [map_function(line) for line in lines if line.strip()]
        top_fechas = reduce_function(mapped_values)
        
        # Convertir las fechas a string para poder serializarlas en JSON
        result = [(fecha.strftime('%Y-%m-%d'), usuario) for fecha, usuario in top_fechas]
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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

    # Ordenar y obtener los top 10
    return sorted(usuarios_top_por_fecha, key=lambda x: len(tweets_por_fecha[x[0]]), reverse=True)[:10]

