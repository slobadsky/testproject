from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def not_in_student_group(user):
    if user:
        return user.groups.filter(name='group_app1').count() == 0
    return False


@login_required(login_url='app1-login-page',redirect_field_name=None)
#@user_passes_test(not_in_student_group, login_url='/app1/')
def index(request):
    return render(request,'app1/index.html',{
            'active_page':'app1-index-page',
            'test':datetime.datetime.now(),
            'ops':list(request.user.groups.values_list('name',flat = True))
            })

def pr_page(request):
    return render(request,'app1/permission-req.html',{
            'test':datetime.datetime.now(),
            })

def login_page(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            uname =request.POST.get('username')
            upass = request.POST.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/app1')
            else:
                messages.error(request,"Invalid username or password.")
                return HttpResponseRedirect('/app1/login')
        else:
            return render(request,'app1/login.html',{})
    else:
        return HttpResponseRedirect('/app1/login')

def logout_page(request):
    logout(request)
    return redirect('/app1/login')