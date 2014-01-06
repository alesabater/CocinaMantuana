from django import forms

""" Formulario de contacto """
class ContactoForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	celular = forms.CharField(max_length=11)
	correo = forms.EmailField(max_length=50)
	mensaje = forms.CharField(max_length=1000)


