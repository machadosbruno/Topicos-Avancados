from django.urls import path
from . import views

urlpatterns = [
    path('instructors/', views.instructors, name='instructors'),
    path('instructors/detailsinstructor/<int:id>', views.detailsinstructor, name='detailsinstructor'),
    path('instructors/addinstructor/', views.addinstructor, name='addinstructor'),
    path('instructors/addinstructor/addrecord/', views.addrecordinstructor, name='addrecordinstructor'),
    path('instructors/deleteinstructor/<int:id>', views.deleteinstructor, name='deleteinstructor'),
    path('instructors/updateinstructor/<int:id>', views.updateinstructor, name='updateinstructor'),
    path('instructors/updateinstructor/updaterecord/<int:id>', views.updaterecordinstructor, name='updaterecordinstructor'),
]
