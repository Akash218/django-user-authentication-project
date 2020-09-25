from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .forms import CreateUserForm,EditProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    else:
        regform = CreateUserForm()
        if request.method=='POST':
            regform=CreateUserForm(request.POST)
        if regform.is_valid():
            regform.save()
            user=regform.cleaned_data.get('username')
            messages.success(request,'Account was Created for' +user)
            return redirect('/accounts/profile')
    return render(request,'registration/register.html',{'regform':regform})
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/accounts/profile')
            else:
                messages.info(request,'Username or password is incorrect')
    return render(request,'registration/login.html')
def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def profile(request):
    return render(request,'registration/profile.html')

@login_required(login_url='login')
def view(request):
    return render(request,'registration/view.html')

@login_required(login_url='login')
def Editprofile(request):
    form=EditProfileForm()
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/accounts/profile')
    return render(request,'registration/update.html',{'form':form})


# Create your views here.
