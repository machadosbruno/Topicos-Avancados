from django.urls import path
from .views import index_view, edit_member_view, delete_member_view

urlpatterns = [
    path('', index_view, name='index'),
    path('edit/<int:member_id>/', edit_member_view, name='edit_member'),
    path('delete/<int:member_id>/', delete_member_view, name='delete_member'),
]
