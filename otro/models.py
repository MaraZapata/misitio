from django.db import models

# Create your models here.
class otro(models.Model):
	nombreProducto = models.CharField(max_length=45, primary_key=True)
	foto = models.ImageField(upload_to='static')
	precio = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombreProducto