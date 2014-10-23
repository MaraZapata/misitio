from django.db import models

# Create your models here.

class pelicula(models.Model):
	nombrePelicula = models.CharField(max_length=45, primary_key=True)
	genero = models.CharField(max_length=45)
	director = models.CharField(max_length=45)
	actores = models.CharField(max_length=45)
	portada = models.ImageField(upload_to='static')
	precio = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombrePelicula