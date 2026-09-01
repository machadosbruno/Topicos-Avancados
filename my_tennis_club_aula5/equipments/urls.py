from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), 
    path('equipments/', views.equipments, name='equipments'),
    path('equipments/details/<int:id>', views.details_equipment, name='details'),
    path('equipments/add/', views.add_equipments, name='add'),
    path('equipments/add/addrecord_equipment/', views.addrecord_equipment, name='addrecord'),
    path('equipments/delete/<int:id>', views.delete_equipment, name='delete'),
    path('equipments/update/<int:id>', views.update_equipment, name='update'),
    path('equipments/update/updaterecord_equipment/<int:id>', views.updaterecord_equipment, name='updaterecord'),
]
