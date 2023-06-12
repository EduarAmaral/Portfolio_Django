from django.shortcuts import render


# Create your views here.

def area_cad(request):
    Navbar = "Seja muito bem vindo"
    Nome = "Eduardo Amaral"

    return render(request, 'area_cad.html', {'Navbar': Navbar, 'Nome': Nome})
