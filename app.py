from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "clave_secreta"

db = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="root",       
    database="portfolio_db"
)
cursor = db.cursor(dictionary=True)

portfolio_data = {
    "skills": ["HTML", "CSS", "Python"],
    "projects": [{"titulo": "Portfolio", "descripcion": "Sitio web personal"}]
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        password = request.form['password']

        if usuario == "admin" and password == "1234":
            session['usuario'] = usuario
            return redirect(url_for('edit'))
        else:
            return render_template('login.html', error="Usuario o contraseña incorrectos")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route('/edit')
def edit():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('edit.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
