from django.shortcuts import render, get_object_or_404, redirect
from menu.models.menu_model import Menu
from plat.models import Plat
from .menu_views import MenuForm  
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})

# Créer un menu
def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'menu/menu_form.html', {'form': form})

# Modifier un menu
def menu_update(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/menu_form.html', {'form': form})

# Supprimer un menu
def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_confirm_delete.html', {'menu': menu})
