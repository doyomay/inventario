from django.shortcuts import render_to_response, get_object_or_404

from django.template.context import RequestContext
from models import *
# Create your views here.
def home(request):
	productos = Productos.objects.all()
	template = "index.html"
	return render_to_response(template,locals())

def producto(request,id_producto):
	provedores = Provedor.objects.all() ##obtenemos la lista de todas las categorias
	pro = get_object_or_404(Provedor,pk=id_producto)## uso de error 404 automatico, pasamos el modelo a comparar y el id
	productos = Productos.objects.filter(provedor = pro)
	template = "index.html"
	return render_to_response(template,locals())
