from django.shortcuts import render
from models import *
from forms import ContactoForm
from django.core.mail import send_mass_mail
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

def index(request):

	return render(request, 'index.html')


""" llama a productos.html y le pasa todos los Productos """
def productos(request):

	productos = Producto.objects.all()

	return render(request, 'productos.html', {'productos':productos})


""" llama a encuentranos.html y le pasa todos los Clientes """
def encuentranos(request):

	clientes = Cliente.objects.all()

	return render(request, 'encuentranos.html',{'clientes':clientes})

def contacto(request):

	return render(request, 'contacto.html')

""" llama a encuentranos-detalle.html y le pasa todos los Cliente que recibe como parametro id """
def encuentranosdetalle(request, id=''):

	cliente = Cliente.objects.get(id=id)
	return render(request, 'encuentranos-detalle.html', {'cliente':cliente})


""" Metodo para enviar correo de contacto """
@csrf_protect
def enviarMail(request):

	if request.method == 'POST':

		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			nombre = formulario.cleaned_data['nombre']
			correo = formulario.cleaned_data['correo']
			mensaje = formulario.cleaned_data['mensaje'] + "\n" + formulario.cleaned_data['correo'] + "\n" + formulario.cleaned_data['celular']

			""" direcciones de correo a enviar correo de contacto """
			datatuple = (
    		(nombre, mensaje, correo, ['ale.sabaterc@gmail.com']),
    		(nombre, mensaje, correo, ['ale.sabaterc@gmail.com']),
			)

			send_mass_mail(datatuple)

			return render(request, 'index.html')

	else:

		formulario = ContactoForm()

	return render(request, 'contacto.html', {'formulario': formulario})

def eventos(request):

	return render(request, 'eventos.html')



# Create your views here.
