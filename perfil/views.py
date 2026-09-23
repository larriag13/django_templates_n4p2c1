from django.shortcuts import render

# Create your views here.
def perfil_uno(request):
    data={"nombre":"Mario","año":1980,"correo":"mario@example.com"}
    return render(request, 'perfil/p1.html',data)

def perfil_dos(request):
    data={"nombre":"Luigi","año":1990,"correo":"luisa@example.com","foto":"luigi.png"}
    return render(request, 'perfil/p2.html',data)