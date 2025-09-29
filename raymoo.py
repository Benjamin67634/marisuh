from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
              <h1>Bienvenidos a esta calculadora virtual hecha en flask!</h1>
              <hp>1.- para sumar teclea la siguiente ruta en el navegador http://127.0.0.1:5000/sumar/[algun valor]/[algun valor]</p>
              <hp>1.- para restar teclea la siguiente ruta en el navegador http://127.0.0.1:5000/restar/[algun valor]/[algun valor]</p>
              <hp>1.- para multiplicar teclea la siguiente ruta en el navegador http://127.0.0.1:5000/mult/[algun valor]/[algun valor]</p>
              <hp>1.- para dividir teclea la siguiente ruta en el navegador http://127.0.0.1:5000/divi/[algun valor]/[algun valor]</p>
              <hp>1.- para sacar el valor maximo de dos numeros teclea la siguiente ruta en el navegador http://127.0.0.1:5000/max/[algun valor]/[algun valor]</p>
              <hp>1.- para sacar el valor minimo de dos numeros teclea la siguiente ruta en el navegador http://127.0.0.1:5000/min/[algun valor]/[algun valor]</p>
              <hp>1.- para sacar el factorial de un numero teclea en el navegador http://127.0.0.1:5000/factorial/[algun valor]</p>

              <footer> Creado por daniel benjamin ortega Flores 5-D </footer>
              '''

@app.route('/sumar/<s1>/<s2>')
def sumar(s1, s2):
    suma=int(s1)+int(s2)
    return(f"la suma de los numeros {s1} y {s2} es {suma}")

@app.route('/restar/<r1>/<r2>')
def restar(r1, r2):
    resta=int(r1)-int(r2)
    return(f"la resta de los numeros {r1} y {r2} es {resta}")

@app.route('/mult/<m1>/<m2>')
def mult(m1, m2):
    multi=int(m1)*int(m2)
    return(f"la multiplicacion de los numeros {m1} y {m2} es {multi}")

@app.route('/divi/<d1>/<d2>')
def divi(d1, d2):
    division=float(d1)/float(d2)
    return(f"la division de los numeros {d1} y {d2} es {division}")

@app.route('/max/<max1>/<max2>')
def max(max1, max2):
    maxresult = 0
    if(int(max1) > int(max2)):
        maxresult = max1
    else:
        if(int(max2) > int(max1)):
            maxresult = max2
    return(f"el numero mas grande de {max1} y {max2} es {maxresult}")

@app.route('/min/<min1>/<min2>')
def min(min1, min2):
    minresult = 0
    if(int(min1) < int(min2)):
        minresult = min1
    else:
        if(int(min2) < int(min1)):
            minresult = min2
    return(f"el numero mas pequeño de {min1} y {min2} es {minresult}")

@app.route('/factorial/<v1>')
def factorial(v1):
    f=1
    for x in range(1,int(v1)+1):
        f*=x
    
    
    return(f"El factorial de {v1}! es {f}")

if __name__  == "__main__":
    app.run(debug=True)

si hay cosas raras es que se me colaron comentarios de su clase
