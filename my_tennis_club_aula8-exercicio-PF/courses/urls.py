from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/detailscourse/<int:id>', views.detailscourse, name='detailscourse'),
    path('courses/addcourse/', views.addcourse, name='addcourse'),
    path('courses/addcourse/addrecord/', views.addrecordcourse, name='addrecordcourse'),
    path('courses/deletecourse/<int:id>', views.deletecourse, name='deletecourse'),
    path('courses/updatecourse/<int:id>', views.updatecourse, name='updatecourse'),
    path('courses/updatecourse/updaterecord/<int:id>', views.updaterecordcourse, name='updaterecordcourse'),
]
