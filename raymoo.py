from flask import Flask

app = Flask(__name__)

@app.route('/') #nombre de la ruta, inicio
def hola_mundo(): #funcionalidad, funcion
    return "<h1> Hola mundo desde flask</h1>"

if __name__  == "__main__":
    app.run(debug=True)