from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import storage
from datetime import datetime
from collections import defaultdict, Counter
import json
from typing import List, Tuple, Optional
import os
import emoji
import re

app = Flask(__name__)
CORS(app)

# Configurar el cliente de Google Cloud Storage
storage_client = storage.Client()

# Get the environment variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello_world():
    return 'Hello, World!'

def map_mentions(content: str) -> List[Tuple[str, int]]:
    user_mentions_counter = Counter()

    for line in content.split('\n'):
        try:
            tweet = json.loads(line)
            user_mentions = re.findall(r'@(\w+)', tweet['content'])
            user_mentions_counter.update(user_mentions)
        except json.JSONDecodeError as e:
            print(f"Error decodificando JSON: {e}")

    return user_mentions_counter.items()

def reduce_mentions(mapped_mentions: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    user_mentions_counter = Counter()
    for user, count in mapped_mentions:
        user_mentions_counter[user] += count

    top_user_mentions = user_mentions_counter.most_common(10)
    return top_user_mentions

@app.route('/q3_time', methods=['POST'])
def q3_time_endpoint():
    request_data = request.get_json()
    bucket_name = request_data['bucket_name']
    blob_name = request_data['blob_name']
    
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        content = blob.download_as_text()
        
        mapped_mentions = map_mentions(content)
        top_user_mentions = reduce_mentions(mapped_mentions)
        
        adapted_output = [(user, count) for user, count in top_user_mentions]
        
        return jsonify(adapted_output)
    except Exception as e:
        return jsonify({'error': str(e)}), 500