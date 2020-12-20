from django.urls import path
from . import views

urlpatterns = [
    path('room_form_add/', views.room_form_add, name='room_form_add'),
    path('room_add/', views.room_add, name='room_add'),
    path('room_list/', views.room_list, name='room_list'),
    path('room_edit/<int:room_id>', views.room_edit, name='room_edit'),
    path('room_delete/<int:room_id>', views.room_delete, name='room_delete'),
    path('room_accept/<', views.room_accept, name='room_accept')
    # path('booking/', views.bookingroom, name='bookingroom'),
    
]