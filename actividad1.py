from flask import Flask, render_template
from flask import request

import forms

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def iniciar():
    numero = 0
    num_form = forms.Numero(request.form)
    if request.method == 'POST':
        numero =  int(request.form.get("numero"))
    return render_template("Actividad1.html", num = numero, form = num_form)
    
@app.route("/resultado", methods=["POST"])
def generarResultado():
    elementos = request.form.getlist("num")
    for i in range(0, len(elementos)):
        elementos[i] = int(elementos[i])
    numMin = min(elementos)
    numMax = max(elementos)
    prom = sum(elementos)/len(elementos)
    duplicados = {}
    alertas = []
    for num in elementos:
        if num in duplicados:
            duplicados[num] += 1
        else:
            duplicados[num] = 1

    for num, cantidad in duplicados.items():
        if cantidad > 1:
            alertas.append("El número {} se repite {} veces.".format(num, cantidad))

    listResult = {'minimo': numMin, 
                  'maximo':numMax, 
                  'promedio': prom,
                  'listaRep': alertas
                  }
        
    return render_template('resultado.html', lista = listResult)


if __name__ =="__main__":
    app.run(debug=True, port=5000)