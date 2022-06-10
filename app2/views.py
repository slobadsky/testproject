from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='app2-login-page',redirect_field_name=None)
def index(request):
    if request.user.groups.filter(name='group_app2').exists():
        #print(request.user.groups.values_list('name',flat = True)[0])
        return render(request,'app2/index.html',{
                'active_page':'app2-index-page',
                'test':datetime.datetime.now(),
                'ops':list(request.user.groups.values_list('name',flat = True))
                })
    else:
        return render(request,'app2/permission-req.html',{})

def pr_page(request):
    return render(request,'app2/permission-req.html',{
            'test':datetime.datetime.now(),
            })


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Manual code to Check whether username is valid or not
        try:
            myuser = User.objects.get(username=username)
        except:
            myuser = False

        if myuser == False:
            mypass = False
        else:
            mypass = myuser.check_password(password)
        user = authenticate(username=username, password=password)
        if myuser != False:
            if user is not None:
                if user.groups.values_list('name',flat = True)[0] == "group_app1":
                    login(request,user)
                    return HttpResponseRedirect('/app1')
                elif user.groups.values_list('name',flat = True)[0] == "group_app2":
                    login(request,user)
                    return HttpResponseRedirect('/app2')
                else:
                    pass
            else:
                messages.error(request, "Le mot de passe incorrect")
                return HttpResponseRedirect('/app2/login')
        else:
            messages.error(request, "L'identifiant incorrect")
            return HttpResponseRedirect('/app2/login')    
        
    if request.user.is_authenticated:
        return HttpResponseRedirect('/app2')
    else:
        return render(request,'app2/login.html',{})

    


def logout_page(request):
    logout(request)
    return redirect('/app2/login')