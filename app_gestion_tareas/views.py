from django.shortcuts import render, redirect
from .forms import TareaForm
from .models import Tarea

def eliminar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('lista_tareas')

def lista_tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST) 
        if form.is_valid():            
            form.save()                
            return redirect('lista_tareas')
    else:
  
        form = TareaForm()            

    tareas = Tarea.objects.all()       
    
    return render(request, 'app_gestion_tareas/gestion.html', {
        'form': form,
        'tareas': tareas
    })