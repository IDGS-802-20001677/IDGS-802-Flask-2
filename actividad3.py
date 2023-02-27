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
    cb1=''
    cb2=''
    cb3=''
    cbt=''
    tolerancia=0
    resultadox=0
    resultadoFMin=0
    resultadoFMax=0
    succes_message='Cálculo realizado con éxito'
    if request.method == 'POST' and form.validate():
        b1 = form.b1.data
        print(b1)
        if b1=='0':
            cb1='#000000'
        elif b1=='1':
            cb1='#800000'
        elif b1=='2':
            cb1='#FF0000'
        elif b1=='3':
            cb1='#FF5733'
        elif b1=='4':
            cb1='#FEFF33'
        elif b1=='5':
            cb1='#5AFF33'
        elif b1=='6':
            cb1='#33A4FF'
        elif b1=='7':
            cb1='#D233FF'
        elif b1=='8':
            cb1='#8E8491'
        elif b1=='9':
            cb1='#FFFFFF'
        b2 = form.b2.data
        print(b2)
        if b2=='0':
            cb2='#000000'
        elif b2=='1':
            cb2='#800000'
        elif b2=='2':
            cb2='#FF0000'
        elif b2=='3':
            cb2='#FF5733'
        elif b2=='4':
            cb2='#FEFF33'
        elif b2=='5':
            cb2='#5AFF33'
        elif b2=='6':
            cb2='#33A4FF'
        elif b2=='7':
            cb2='#D233FF'
        elif b2=='8':
            cb2='#8E8491'
        elif b2=='9':
            cb2='#FFFFFF'
        b3 = form.b3.data
        print(b3)
        if b3=='1':
            cb3='#000000'
        elif b3=='10':
            cb3='#800000'
        elif b3=='100':
            cb3='#FF0000'
        elif b3=='1000':
            cb3='#FF5733'
        elif b3=='10000':
            cb3='#FEFF33'
        elif b3=='100000':
            cb3='#5AFF33'
        elif b3=='1000000':
            cb3='#33A4FF'
        elif b3=='10000000':
            cb3='#D233FF'
        elif b3=='100000000':
            cb3='#8E8491'
        elif b3=='1000000000':
            cb3='#FFFFFF'
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
            cbt='#7B7637'
        elif tolerancia==0:
            resultadoFMin=float(float(resultadox)-float(resultadox)*0.10)
            resultadoFMax=float(float(resultadox)+float(resultadox)*0.10)
            print(resultadoFMin)
            print(resultadoFMax)
            cbt='#A0A0A0'        
        flash(succes_message)
    return render_template("actividad3.html", form = form,
                               b1=b1, b2=b2, b3=b3, tolerancia=tolerancia,
                               resultadoFMin=resultadoFMin, resultadox=resultadox,
                               resultadoFMax=resultadoFMax, cb1=cb1, cb2=cb2, cb3=cb3,
                               cbt=cbt)
    



if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=5000)