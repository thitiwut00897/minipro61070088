from builtins import object
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from booking.models import Rooms
from .models import *

# from .models import *
# Create your views here.
def room_form_add(request):
    if request.method == "POST":
        createuser = ''
        createuser = Rooms.objects.create(
            name = request.POST.get('name'),
            open_time = request.POST.get('start'),
            close_time = request.POST.get('stop'),
            capacity = request.POST.get('capacity')
        )
        return redirect('room_list')


@login_required(login_url='login')
def room_list(request):
    # search = repuest.GET.get('search', '')
    # room = Rooms.objects.filter(Q(name__icontains=search)).order_by('name')        search----------------------------------

    room = Rooms.objects.all()
    context={
        'room':room
    }
    return render(request, 'rooms/room_list.html',context=context)

# def room_update(request):
#     pass

@permission_required('booking.rooms.Can_add_rooms') 
def room_add(request):
    return render(request, 'rooms/room_form.html')

@permission_required('booking.rooms.Can_change_rooms')  
def room_edit(request, room_id):
    return render(request, 'rooms/room_form.html') 

@permission_required('booking.rooms.Can_delete_rooms') 
def room_delete(request, room_id):
    Rooms.objects.get(pk=room_id).delete()
    # return render(request, 'rooms/room_form.html')
    return redirect('room_list')
    
@login_required(login_url='login')
def room_accept(request):
    return render(request, 'rooms/room_accept.html')