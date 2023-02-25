from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, EmailField
from wtforms.fields import TextAreaField
from wtforms import validators, RadioField, PasswordField


class UserForm(Form):
    matricula=StringField("Matrícula",[validators.DataRequired(message='La matrícula es requerida')])
    nombre=StringField("Nombre", [validators.DataRequired(message='El campo es requerido'),validators.length
                                  (min=5, max=15, message="Nombre inválido")])
    Apaterno=StringField("Apaterno")
    Amaterno=StringField("Amaterno")
    email=EmailField("Correo")

class Numero(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Campo requerido')])
        
class Palabras(Form):
    palabraIngles=StringField("palabraIngles",[validators.DataRequired(message='La palabra en inglés es requerida')])
    palabraEspaniol=StringField("palabraEspaniol",[validators.DataRequired(message='La palabra en español es requerida')])
    
class TraductorForm(Form):
    espanol = StringField('Palabra en español:',
    [
        validators.DataRequired(message="El campo es requerido"),
    ])
    ingles = StringField('Palabra en inglés:',
    [
        validators.DataRequired(message="El campo es requerido"),
    ])

class BuscarForm(Form):
    palabra = StringField('Traducción al idioma seleccionado:',
    [
        validators.DataRequired(message="El campo es requerido"),
    ])
    idioma =  RadioField('Selecciona el idioma:',
                         choices=[(1,'Inglés'),(0,'Español')])
    
class LoginForm(Form):
    username = StringField('usuario',[
        validators.data_required(message = 'El usuario es requerida')]
                            )
    password = PasswordField('contraseña', [validators.DataRequired(message='El campo es requerido'),
                            validators.length(min=5, max=15, message='Ingresa un numero minimo')]
                        )