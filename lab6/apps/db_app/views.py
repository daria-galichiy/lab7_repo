from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.views.generic import ListView
from lab6.apps.db_app.models import *
from django.contrib.auth.models import User
from lab6.apps.db_app.registration import *
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    return render(request, 'main_page.html')


class CountriesList(ListView):
    model = Countries
    template_name = "countries.html"


class ActorsList(ListView):
    model = Actors
    template_name = "actors.html"


class FilmmakersList(ListView):
    model = Filmmakers
    template_name = "filmmakers.html"


class Film_writersList(ListView):
    model = Film_writers
    template_name = "film_writers.html"


class ProducersList(ListView):
    model = Producers
    template_name = "producers.html"


class CameramenList(ListView):
    model = Cameramen
    template_name = "cameramen.html"


class FilmsList(ListView):
    model = Films
    template_name = "films.html"


def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'surname': '', 'firstname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Пожалуйста, введите логин.'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Длина логина должна превышать 5 символов.'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует.'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Пожалуйста, введите пароль.'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов.'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать.'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Пожалуйста, введите e-mail.'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Пожалуйста, введите фамилию.'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Пожалуйста, введите имя.'
        if not error_flag:
            user = User.objects.create_user(username=username, password=password, email=email,
                                            last_name=surname, first_name=firstname)
            return HttpResponseRedirect('/db_app/login/')
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/db_app/account/')
        else:
            error = "Неверный логин или пароль."
    return render(request, 'login.html', locals())


@login_required()
def account(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/db_app/login/')
    else:
        return render(request, 'account.html', locals())


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            last_name=request.POST.get('surname'),
                                            first_name=request.POST.get('firstname'))
            return HttpResponseRedirect('/db_app/login/')
        else:
            form = RegistrationForm()
    return render(request, 'registration2.html', {'form': form})
