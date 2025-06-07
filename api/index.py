from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola desde Flask en Vercel!"

# Requerido para Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
