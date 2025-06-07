from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('login.html')


# Ruta corta para dashboard cliente
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/cliente.html')


# Ruta extendida opcional para redirección directa
@app.route('/dashboard/cliente.html')
def cliente_dashboard():
    return render_template('dashboard/cliente.html')


# Ruta para el dashboard de admin (usa admin.html cuando lo crees)
@app.route('/dashboard/admin.html')
def admin_dashboard():
    return render_template('dashboard/admin.html')  # asegúrate de que exista ese archivo


if __name__ == '__main__':
    app.run(debug=True)
