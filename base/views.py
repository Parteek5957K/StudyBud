from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember, User
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, "base/home.html")

@login_required(login_url='login')
def dashboard(request):
    context={'name':request.user.username[0]}
    return render(request, "base/dashboard.html", context)

def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page': page}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def signuppage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Passwords doesn\'t match')
    return render(request, 'base/signup.html')

@login_required(login_url='login')
def solo_study(request):
    return render(request, "base/solo_study.html")

@login_required(login_url='login')
def group_study(request):
    return render(request, "base/group_study.html")

def lobby(request):
    response = render(request, 'base/lobby.html')
    response['X-Frame-Options'] = 'SAMEORIGIN'
    return response

def room(request):
    response = render(request, 'base/room.html')
    response['X-Frame-Options'] = 'SAMEORIGIN'
    return response


# def getToken(request):
#     appId = "7648582615784b55994a0c5d17da74f4"
#     appCertificate = "26e3042d51c84f888ff4b44dbc1dcaba"
#     channelName = request.GET.get('channel')
#     uid = random.randint(1, 230)
#     expirationTimeInSeconds = 3600
#     currentTimeStamp = int(time.time())
#     privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
#     role = 1
#
#     token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
#
#     return JsonResponse({'token': token, 'uid': uid}, safe=False)
#

# @csrf_exempt
# def createMember(request):
#     data = json.loads(request.body)
#     member, created = RoomMember.objects.get_or_create(
#         name=data['name'],
#         uid=data['UID'],
#         room_name=data['room_name']
#     )
#
#     return JsonResponse({'name':data['name']}, safe=False)
#
#
# def getMember(request):
#     uid = request.GET.get('UID')
#     room_name = request.GET.get('room_name')
#
#     member = RoomMember.objects.get(
#         uid=uid,
#         room_name=room_name,
#     )
#     name = member.name
#     return JsonResponse({'name':member.name}, safe=False)
#
# @csrf_exempt
# def deleteMember(request):
#     data = json.loads(request.body)
#     member = RoomMember.objects.get(
#         name=data['name'],
#         uid=data['UID'],
#         room_name=data['room_name']
#     )
#     member.delete()
#     return JsonResponse('Member deleted', safe=False)
