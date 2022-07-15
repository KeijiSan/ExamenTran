from sqlite3 import DateFromTicks
from django.shortcuts import render

from front.models import Producto

# Create your views here.
def index(request):
    return render(request, 'index.html')
def api(request):
    return render(request,'api.html')
def index(request):
    fotos=Producto.objects.all()
    datos={'producto':fotos}
    return render(request,'index.html',datos)