from flask import Flask, Response, send_from_directory, request, jsonify
from loguru import logger as log
import sys

DIRECTORY = './webserver/web'
app = Flask("Webserver", static_url_path='/', static_folder=DIRECTORY)

@app.route('/')
def send_root():
    log.info('Request: {}', request)
    return send_from_directory(DIRECTORY, 'index.html')

def main():
    try:
        arg = sys.argv[1]
        HOST, PORT = arg.split(':')
    except Exception as e:
        print('Usage: python main.py <HOST>:<PORT>')
        return
    app.run(host=HOST, port=PORT)

main()

