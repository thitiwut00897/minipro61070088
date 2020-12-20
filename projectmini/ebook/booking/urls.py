from django.urls import path
from booking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:roomid>', views.detail, name='detail'),
    path('booking/', views.bookingroom, name='bookingroom'),
    
]