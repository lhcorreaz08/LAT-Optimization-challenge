from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import storage
from datetime import datetime
from collections import defaultdict, Counter
import json
from typing import List, Tuple, Optional
import os
import emoji

app = Flask(__name__)
CORS(app)

# Configurar el cliente de Google Cloud Storage
storage_client = storage.Client()

# Get the environment variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello_world():
    return 'Hello, World!'


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

@app.route('/q2_memory', methods=['POST'])
def q2_memory_endpoint():
    # Recibir el nombre del bucket y el blob_name en el cuerpo de la solicitud
    request_data = request.get_json()
    bucket_name = request_data['bucket_name']
    blob_name = request_data['blob_name']
    
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        # Descargar el contenido del blob como texto
        content = blob.download_as_text()

        # Procesar el contenido como si fuera un archivo
        result = q2_time_from_content(content)
        # Convertir el resultado a un formato que pueda ser serializado en JSON
        result_json = [{"emoji": emoji, "count": count} for emoji, count in result]
        
        return jsonify(result_json)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def q2_time_from_content(content: str) -> List[Tuple[str, int]]:
    mapped_values = []

    # Procesar cada línea del contenido
    for line in content.split('\n'):
        mapped_values.extend(map_function(line))

    shuffled_data = shuffle_and_sort(mapped_values)
    reduced_data = reduce_function(shuffled_data)

    return reduced_data