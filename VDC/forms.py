from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(Form):
	name = StringField("Nombre", [InputRequired("Por favor ingrese su nombre.")])
	email = StringField("Correo Electronico", [InputRequired("Por favor ingrese su correo electronico."), Email("Por favor ingrese su correo electronico.")])
	subject = StringField("Asunto", [InputRequired("Por favor ingrese el encabezado.")])
	message = TextAreaField("Mensage", [InputRequired("Por favor ingrese su mensaje.")])
	submit = SubmitField("Enviar")

# Subscribae

class Subscribe(Form):
	email = StringField("Correo Electronico", [InputRequired("Ingrese su correo electronico"), Email("Subscribase")])
	submit = SubmitField("Eviar")



