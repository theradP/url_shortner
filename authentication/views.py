from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    auth.login(request, user)
                    if request.POST['next'] != '':
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/')
                except User.DoesNotExist:
                    return render(request, 'login.html', {'error': 'User does not exist'})
            else:
                return render(request, 'login.html', {'error': 'Empty Fields'})
        else:
            return render(request, 'login.html')
    else:
        return redirect('/')





def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['password'] == request.POST['password2']:
                if request.POST['username'] and request.POST['email'] and request.POST['password']:
                    try:
                        user = User.objects.get(email=request.POST['email'])
                        return render(request, 'signup.html', {'error': 'User already exists'})
                    except User.DoesNotExist:
                        User.objects.create_user(
                            username=request.POST['username'],
                            email=request.POST['email'],
                            password=request.POST['password']
                        )
                        messages.success(request, "Signup successful \n Login Here")
                        return redirect(login)
                else:
                    return render(request, 'signup.html', {'error': 'Empty fields'})
            else:
                return render(request, 'signup.html', {'error': 'Passwords do not match'})
        else:
            return render(request, 'signup.html')
    else:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/login')