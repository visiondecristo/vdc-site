from VDC import app
from flask import render_template, request, flash, redirect, url_for
from forms import ContactForm, Subscribe
from flask_mail import Mail, Message


mail = Mail()


# Index route
@app.route('/')
def inicio():
	return render_template('index.html')

# Radio route
@app.route('/radio')
def radio():
	return render_template ('radio.html')

# Blog route
@app.route('/blog')
def blog():
	return render_template ('blog.html')

# Nosotros route
@app.route('/nosotros')
def nosotros():
	return render_template ('nosotros.html')

# Gracias route
@app.route('/gracias')
def gracias():
	return render_template('gracias.html')

# Galeria route
@app.route('/galeria')
def galeria():
	return render_template('galeria.html')


#Contact form
@app.route('/contactenos', methods=['GET', 'POST'])
def contactenos():
	form = ContactForm()
	if form.validate_on_submit():
		msg = Message(form.subject.data, sender='ADMIN', recipients=['contactenos@visiondecristo.org'])
		msg.body = """
		From: %s <%s>
		%s
		""" % (form.name.data, form.email.data, form.message.data)
		mail.send(msg)

		return redirect( url_for('gracias') )
	else:
		return render_template('contactenos.html', form=form)

