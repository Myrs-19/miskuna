from winreg import QueryValue
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import *
from .forms import *
from .logic import *

def index(request):
    # данные для формсета, если уже были заполнены поля, то данные, которые были заполнены, сохранятся по ключу form-N-text 
    data = {
        'form-TOTAL_FORMS' : '2',
        'form-INITIAL_FORMS' : '0',
        'form-0-text' : '',
        'form-1-text' : '',
    }
    formset = formset_factory(FormTask, extra=2)

    if request.method == "POST":
        last_item = list(request.POST.keys())[-1]

        if 'add_field' == last_item:
            for key, item in request.POST.items(): #переименовать item <- задача для программиста, для тебя блять еблан
                if 'form' in key:
                    data[key] = item
            #минус crsf токен
            add = len(request.POST) - 1
            data['form-TOTAL_FORMS'] = str(add)
            formset = formset_factory(FormTask, extra=add) #перегружаем formset для количества add

        if 'new_panel' == last_item:
            # if request
            save_panel(request)

        if 'change' == last_item:
            t = change_panel(request)

        if 'del-panel' == last_item:
            Panel.objects.get( id = request.POST[last_item]).delete()
        
        # возвращает пустую строку если нет объект не найден
        if get_key_for_del(request):
            task_item = get_key_for_del(request)
            del_task(request.POST[ task_item ]) #передаем pk таска который удаляем
            


    # form = FormTask()
    content = {
        'panels' : Panel.objects.filter(user_id=request.user.pk),
        # 'form' : form,
        'formset' : formset(data),
        'g' : request.GET,
        'p' : request.POST,
    }

    return render(request, "notes/index.html", content)



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Регистрация прошло успешно')
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    content = {
        "form" : form,
    }
    return render(request, "notes/register.html", content)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    content = {
        "form" : form,
    }
    return render(request, "notes/login.html", content)



def user_logout(request):
    logout(request)
    return redirect('login')