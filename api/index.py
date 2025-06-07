from flask import Flask, jsonify
from vercel_wsgi import handle_request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"mensaje": "Backend Python de COAFIN funcionando correctamente en Vercel 🚀"})

# Requerido por Vercel
def handler(environ, start_response):
    return handle_request(app, environ, start_response)

