from flask import Flask, render_template, redirect, url_for
from flask import request
import forms

app=Flask(__name__)

@app.route("/traductor", methods=['GET', 'POST'])
def traductor():
    form = forms.TraductorForm(request.form)
    form1 = forms.BuscarForm(request.form)
    if request.method == 'POST' and form.validate():
        espanol = form.espanol.data.lower()
        ingles = form.ingles.data.lower()
        f = open("traductor.txt", "a")
        f.write(f"{espanol},{ingles}\n")
        f.close()
        return redirect(url_for('traductor'))
    elif request.method == 'POST' and form1.validate():
        idioma = int(form1.idioma.data)
        palabra = form1.palabra.data.lower()
        f = open("traductor.txt", "r")
        palabras = f.readlines()
        f.close()
        palabra_traducida = "La palabra no está registrada"
        for p in palabras:
            if palabra in p:
                palabra_traducida = p.split(',')[idioma]
                break
        return render_template("actividad2.html", form=form, form1 = form1, traduccion = palabra_traducida)
    return render_template("actividad2.html", form=form, form1 = form1)

'''@app.route("/", methods=["GET"])
@app.route("/diccionario", methods=["GET","POST"])
def Diccionario():
    diccionario=forms.Palabras(request.form)
    palabraIngles=''
    palabraEspaniol=''
    DICCIONARIO={
    "amarillo":"yellow",
    "casa":"house",
    "mesa":"table",
    "puerta":"door",
    }
    mat=diccionario.palabraIngles.data
    
    
    while request.method=='POST' and diccionario.validate():
        print (diccionario.palabraIngles.data)
        palabraIngles =  str(request.form.get("palabraIngles"))
        palabraEspaniol =  str(request.form.get("palabraEspaniol"))
    
        print (palabraIngles)
        print (palabraEspaniol)
        
        if DICCIONARIO.get(palabraIngles)==None:
            DICCIONARIO.update({palabraEspaniol:palabraIngles})
            print(DICCIONARIO)
            break
            
    return render_template("actividad2.html", form=diccionario)'''


if __name__=="__main__":
    app.run(debug=True, port=3000)