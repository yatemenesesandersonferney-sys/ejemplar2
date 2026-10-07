from django.urls import path
from . views import lista_tareas, eliminar_tarea

urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),
    path("eliminar_tarea/<int:id>/", eliminar_tarea, name="eliminar_tarea"),
]
