from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from plat.forms.plat_forms import PlatForm
from plat.models.plat_model import Plat

def plat_list(request):
    plats = Plat.objects.all()
    return render(request, 'plat/plat_list.html', {'plats': plats})

def plat_create(request):
    if request.method == 'POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plat_list')
    else:
        form = PlatForm()
    return render(request, 'plat/plat_form.html', {'form': form})

def plat_update(request, pk):
    plat = get_object_or_404(Plat, pk=pk)
    if request.method == 'POST':
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('plat_list')
    else:
        form = PlatForm(instance=plat)
    return render(request, 'plat/plat_form.html', {'form': form})

def plat_delete(request, pk):
    plat = get_object_or_404(Plat, pk=pk)
    if request.method == 'POST':
        plat.delete()
        return redirect('plat_list')
    return render(request, 'plat/plat_confirm_delete.html', {'plat': plat})
