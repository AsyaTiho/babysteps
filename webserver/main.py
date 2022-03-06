from flask import Flask, send_from_directory, request, jsonify
from loguru import logger as log
import sys, os

DIRECTORY = './webserver/web'
API_EP = '/api/v1'
app = Flask("Webserver", static_url_path='/', static_folder=DIRECTORY)

@app.route(API_EP + '/poor_ratio', methods=['POST'])
def poor_ratio():
    log.info('Request: {}', request)
    log.info('Request json: {}', request.json)
    import random
    ratio = random.random()
    return jsonify({"ratio": ratio})

@app.route('/')
def send_root():
    log.info('Request: {}', request)
    return send_from_directory(DIRECTORY, 'index.html')

def main():
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 5000))
    log.info('Running on {}:{}', HOST, PORT)
    app.run(host=HOST, port=PORT)

main()

