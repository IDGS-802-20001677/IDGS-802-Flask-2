from flask import Flask, render_template, make_response, flash
from flask import request
from flask_wtf.csrf import CSRFProtect
import forms

app=Flask(__name__)
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf=CSRFProtect()

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'),404

@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get('datos_user')
    nombre=valor_cookie.split('@')
    return render_template('saludo.html', nom=nombre[0])

@app.route("/formulario2", methods=["GET"])
def formulario():
    return render_template("formulario2.html")

@app.route("/Alumnos", methods=["GET","POST"])
def Alumno():
    alum_form=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method=='POST' and alum_form.validate():
        mat=alum_form.matricula.data
        nom=alum_form.nombre.data
        #alum_form=forms.apaterno.data
        #alum_form=forms.amaterno.data
        #alum_form=forms.email.data
    return render_template("Alumnos.html", form=alum_form, mat=mat,nom=nom)


@app.before_request()
def before_request():
    print('numero1')

@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    print('numero2')
    reg_user = forms.LoginForm(request.form)
    datos=''
    if request.method == 'POST' and reg_user.validate():
       user=reg_user.username.data
       passw=reg_user.username.data
       datos=user+'@'+passw
       succes_message='Bienvenido {}'.format(user)
       flash(succes_message)
        
    response=make_response(render_template("cookies.html", form = reg_user))
    response.set_cookie('datos_user',datos)
    return response

@app.after_request()
def after_request(response):
    print('numero3')
    return response

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)