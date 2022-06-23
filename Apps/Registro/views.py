from mailbox import NoSuchMailboxError
from django.shortcuts import render, redirect
from.models import Info
from django.contrib import messages  #Libreria de django para enviar mensajes


# Create your views here.

def home(request):
    empresaslistado = Info.objects.all()  #Retornara el listado de todos los cursos
    return render(request, "gestionInfo.html", {"empresaslis": empresaslistado}) #Recuperamos empresas en la plantilla

def registrarEmpresa(request):
    empresa=request.POST['txtEmpresa']
    direccion=request.POST['txtDirección']
    nit=request.POST['txtNit']
    telefono=request.POST['txtTeléfono']

    empresa2=Info.objects.create(empresa=empresa, direccion=direccion, nit=nit, telefono=telefono)
    return redirect('/') #Regrese a la ruta inicial

def edicionEmpresa(request, nit):
    empresa=Info.objects.get(nit=nit)
    return render(request, "edicionEmpresa.html", {"empresa":empresa})

def editarEmpresa(request):
    empresa=request.POST['txtEmpresa']
    direccion=request.POST['txtDirección']
    nit=request.POST['txtNit']
    telefono=request.POST['txtTeléfono']

    empresa2=Info.objects.get(nit=nit)
    empresa2.empresa = empresa
    empresa2.direccion = direccion
    empresa2.telefono = telefono
    empresa2.save()  #Función que permite guardar los nuevos valores de empresa
    return redirect('/') #Regrese a la ruta inicial

def eliminarEmpresa(request, nit): #Asigno parametro nit, como referncia y elimirrlo desde el ORM
    empresa2=Info.objects.get(nit=nit) #Verifica que el nit referncia es el que realmente se va a borrar
    empresa2.delete()
    return redirect('/') #Regrese a la ruta inicial