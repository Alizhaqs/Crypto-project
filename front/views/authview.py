from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse


def loginView(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'main-page')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'main-page')
        else:
            error = "Пароль неверный!"
            context={
                'error': error
            }
            return render(request,'front/admin-login.html', context)
    return render(request,
                  'front/admin-login.html',
                  {'next': request.GET.get('next') or reverse('main-page')})


def logoutView(request):
    logout(request)
    return redirect('login')


def forgotPasswordView(request):
    context = {
    }
    return render(request, 'front/admin-forgot-password.html', context=context)


def resetPasswordView(request):
    context = {
    }
    return render(request, 'front/admin-reset-password.html', context=context)


def RegisterView(request):
    context = {

     }
    return render(request, 'front/auth-register.html', context=context)