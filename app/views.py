from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def home(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'un':un}
        return render(request,'home.html',d)
    return render(request,'home.html')


def registration(request):
    USFO=Userform()
    PFO=profileform()
    d={'USFO':USFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFDO=Userform(request.POST)
        PFDO=profileform(request.POST,request.FILES)
       
        if UFDO.is_valid() and PFDO.is_valid():
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()

            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registraion ',
                        'thanks for registering',
                        'vasaveesreerama@gmail.com',
                        [MUFDO.email],
                        fail_silently=False)
            
            return HttpResponse('registration is successful')
        return HttpResponse('data not valid')

    return render(request,'registrations.html',d)

def User_login(request):
    if request.method=='POST':
        username = request.POST['un']
        password = request.POST['pw']
        AUO = authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('NOT DONE')

    return render(request,'user_log.html')

@login_required
def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))




@login_required
def change_password(request):
    if request.method=='POST':
        password=request.POST['pw']
        rpassword=request.POST['re-pw']
        if password==rpassword:
            un=request.session.get('username')
            uo=User.objects.get(username=un)
            uo.set_password(password)
            uo.save()
            return HttpResponse('<h1>password changed successfully</h1>')
        return HttpResponse('<h1>password not match</h1>')
    return render(request,'changepassword.html')


def forgot_password(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        rpassword=request.POST['re-pw']
        ufo=User.objects.filter(username=username)
        if password==re-password and len(ufo)>0:
            uo=ufo[0]
            uo.set_password(password)
            uo.save()
            return HttpResponse('<h1>password changed successfully</h1>')
        return HttpResponse('<h1>password not match or user not matched </h1>')

    return render(request,'forgot_password.html')


@login_required
def details_required(request):
    un=request.session.get('username')
    uo=User.objects.get(username=un)
    po=profile.objects.get(username=uo)
    d={'uo':uo,'po':po}
    return render(request,'userdetails.html',d)
    