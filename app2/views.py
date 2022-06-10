from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


def not_in_student_group(user):
    if user:
        if user.groups.filter(name='group_app2').exists():
            return True
        else:
            return False


@login_required(login_url='app2-login-page',redirect_field_name=None)
@user_passes_test(not_in_student_group, login_url='app2-login-page')
def index(request):
    print(request.user.groups.filter(name='group_app1').exists())
    #print(request.user.groups.values_list('name',flat = True)[0])
    return render(request,'app2/index.html',{
            'active_page':'app2-index-page',
            'test':datetime.datetime.now(),
            'ops':list(request.user.groups.values_list('name',flat = True))
            })

def pr_page(request):
    return render(request,'app2/permission-req.html',{
            'test':datetime.datetime.now(),
            })

def login_page(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            uname =request.POST.get('username')
            upass = request.POST.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:                
                if user.groups.values_list('name',flat = True)[0] == "group_app2":
                    login(request,user)
                    return HttpResponseRedirect('/app2')
                else:
                    messages.error(request,"Unautorised group.")
                    return HttpResponseRedirect('/app2/login')   
            else:
                messages.error(request,"Invalid username or password.")
                return HttpResponseRedirect('/app2/login')
        else:
            return render(request,'app2/login.html',{})
    else:
        return HttpResponseRedirect('/app2/login')

def logout_page(request):
    logout(request)
    return redirect('/app2/login')