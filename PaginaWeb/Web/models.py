from django.db import models

class Producto(models.Model):
	p_nombre = models.CharField(max_length=200)
	p_ingredientes = models.CharField(max_length=500, blank=True, null=True)
	p_costo = models.IntegerField()
	p_foto = models.ImageField(upload_to = 'media/', default = 'media/nopic.jpg')
	p_descripcion = models.CharField(max_length=500)

	""" Nombre del objeto Producto """
	def __unicode__(self):
		return self.p_nombre

class Cliente(models.Model):
	c_nombre = models.CharField(max_length=100)
	c_correo = models.EmailField(max_length=100)
	c_direccion = models.CharField(max_length=500, blank=True, null=True)
	c_rif = models.CharField(max_length=15)
	c_tlf_local = models.CharField(max_length=20, blank=True, null=True)
	c_celular = models.CharField(max_length=20, blank=True, null=True)
	c_persona_contacto = models.CharField(max_length=30, blank=True, null=True)
	c_latitud = models.FloatField()
	c_longitud = models.FloatField()
	c_foto1 = models.ImageField(upload_to = 'media/', default = 'media/nopic.jpg')
	c_foto2 = models.ImageField(upload_to = 'media/', default = 'media/nopic.jpg')
	c_foto3 = models.ImageField(upload_to = 'media/', default = 'media/nopic.jpg')
	c_foto4 = models.ImageField(upload_to = 'media/', default = 'media/nopic.jpg')
	c_foto5 = models.ImageField(upload_to = 'media/', default = 'media/nopic.jpg')

	""" Nombre del objeto Cliente """
	def __unicode__(self):
		return self.c_nombre

# Create your models here.
