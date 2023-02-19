from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, EmailField
from wtforms.fields import TextAreaField
from wtforms import validators


class UserForm(Form):
    matricula=StringField("Matrícula",[validators.DataRequired(message='La matrícula es requerida')])
    nombre=StringField("Nombre")
    Apaterno=StringField("Apaterno")
    Amaterno=StringField("Amaterno")
    email=EmailField("Correo")

class NumberForm(Form):
        num = StringField('numeros',      
                    [validators.data_required(message = 'Campo requerido')])
