from builtins import object

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Booking
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Rooms
# from .models import *
# from ebook.form import SignUpForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'register.html', {'forms': form})

def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    context = {}
    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        createuser = ''
        if password1 == password2:
            createuser = User.objects.create_user(
            username = request.POST.get('username'),
            password = request.POST.get('password1'),
            first_name = request.POST.get('firstname'),
            last_name = request.POST.get('lastname'),
            email = request.POST.get('email')
            )
            # group = User.objects.get(name='User')
            # User.groups.add(group)
            return redirect('index')
        else:
            context['error'] = 'passworddonmatch!'
            return render(request, template_name='register.html', context=context)

def register_page(request):
    return render(request,'register.html')



    
@login_required(login_url='login')
def index(request):
    rooms = Rooms.objects.all()
    context={
        'rooms':rooms
    }
#     """s
#         Index page - หน้าจอรายการวิชาที่มีการสอนทั้งหมด
#     """
#     search_txt = request.GET.get('inputSearch', '')
#     print(search_txt)
#     date = request.GET.get('date', '')
#     time = request.GET.get('time', '')

#     classes = ClassRoom.objects.filter(
#         course__name__icontains=search_txt
#     )
#     if date:
#         classes = classes.filter(course__date=date)
#     if time:
#         classes = classes.filter(course__academic_time=time)

    return render(request, 'booking/index.html',context=context)
    # , context={
    #     'search_txt': search_txt,
    #     'date': date,
    #     'time': time,
    #     'classes': classes
    # })
@login_required(login_url='login')
def detail(request, roomid):
    rooms = Rooms.objects.get(pk=roomid)
    # rooms = Rooms.objects.all()
    context={
        'booking':rooms
    }
    return render(request, 'booking/detail.html', context=context)
    
@login_required(login_url='login')
def bookingroom(request):
    if request.method == "POST":
        create = ''
        create = Booking.objects.create(
        date = request.POST.get('date'),
        start_time = request.POST.get('start'),
        end_time = request.POST.get('stop'),
        description = request.POST.get('detail'),

        )
        # print(date)
        # print(start)
        # print(stop)
        # print(detail)
        return redirect('index')

# def register(request):
#     form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

