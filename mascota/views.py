from django.shortcuts import render, redirect
from django.http import HttpResponse

from mascota.forms import MascotaForm
from mascota.models import Mascota

# Create your views here.


def index_mascota(request):
    return render(request, "mascota/index.html")



def mascota_view(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form =  MascotaForm()

    return render(request, "mascota/mascota_form.html", {'form':form})
    



def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id', 'nombre')    
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form': form})    
