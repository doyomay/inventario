from django.db import models

# Create your models here.
class Provedor(models.Model):
	nombre = models.CharField(max_length=140)
	rfc = models.CharField(max_length=140)
	def __unicode__(self):
		return self.nombre

class Productos(models.Model):
	nombre = models.CharField(max_length=140)
	provedor = models.ForeignKey(Provedor)
	existencia = models.BooleanField()
	descripcion = models.CharField(max_length=300)
	precio_pro = models.FloatField(default=0)
	precio_pub = models.FloatField(default=0)
	def __unicode__(self):
		return "%s -- %s " %(self.nombre, self.existencia)
