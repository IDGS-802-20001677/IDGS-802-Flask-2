from flask import Flask, render_template, flash
from flask import request
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)
app.config['SECRET_KEY']="clave encriptada"
csrf=CSRFProtect()

@app.route("/", methods=["GET", "POST"])
def iniciar():
    form = forms.Resistencias(request.form)
    b1=''
    b2=''
    b3=''
    tolerancia=0
    resultadox=0
    resultadoFMin=0
    resultadoFMax=0
    succes_message='Cálculo realizado con éxito'
    if request.method == 'POST' and form.validate():
        b1 = form.b1.data
        print(b1)
        b2 = form.b2.data
        print(b2)
        b3 = form.b3.data
        print(b3)
        tolerancia = int(form.tolerancia.data)
        print(tolerancia)
        resultado=str(b1+b2)
        resultadox=int(int(resultado)*int(b3))
        print(resultado)
        print(resultadox)
        if tolerancia==1:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.05)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.05)
            print(resultadoFMin)
            print(resultadoFMax)
        elif tolerancia==0:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.10)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.10)
            print(resultadoFMin)
            print(resultadoFMax)        
        flash(succes_message)
    return render_template("actividad3.html", form = form,
                               b1=b1, b2=b2, b3=b3, tolerancia=tolerancia,
                               resultadoFMin=resultadoFMin, resultadox=resultadox,
                               resultadoFMax=resultadoFMax)
    



if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=5000)