from flask import Flask, Response, send_from_directory, request, jsonify
from loguru import logger as log
import sys, os

DIRECTORY = './webserver/web'
API_EP = '/api/v1'
app = Flask("Webserver", static_url_path='/', static_folder=DIRECTORY)

@app.route('/')
def send_root():
    log.info('Request: {}', request)
    return send_from_directory(DIRECTORY, 'index.html')

@app.route(API_EP + '/poor_ratio', methods=['POST'])
def poor_ratio():
    log.info('Request: {}', request)
    log.info('Request json: {}', request.json)
    return jsonify({"ratio": 0.5})

def main():
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 5000))
    log.info('Running on {}:{}', HOST, PORT)
    app.run(host=HOST, port=PORT)

main()

