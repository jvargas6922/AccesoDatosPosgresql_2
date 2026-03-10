from django.shortcuts import render

# Create your views here.
def index(request):
    mensaje = "Bienvenido a la página de inicio"
    return render(request, 'index.html', {'mensaje': mensaje})
