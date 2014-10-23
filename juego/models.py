from django.db import models

# Create your models here.
class juego(models.Model):
	nombreJuego = models.CharField(max_length=45, primary_key=True)
	genero = models.CharField(max_length=45)
	compañia = models.CharField(max_length=45)
	portada = models.ImageField(upload_to='static')
	precio = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombreJuego