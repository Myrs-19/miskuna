from winreg import QueryValue
from django.shortcuts import render
from django.forms import formset_factory

from .models import *
from .forms import *

def savePanel(request):
    for key, item in request.POST.items():
        if key == 'form-0-text':
            p = Panel(title=item)
            p.save()
        elif "form" in key:
            t = Task(text=item, panel=p)
            t.save()


# post, change
def changePanel(request):

    tasks = [Task.objects.get(pk=key) for key, value in request.POST.items() if key.isnumeric()]

    # получаем панель которую будет изменять
    panel = Panel.objects.get(pk=request.POST['change'])
    panel.title=request.POST['title']
    panel.save()

    # задачи которые нужно поменять
    for task in tasks:
        task.text = request.POST[str(task.pk)] #type(task.pk) - int, ключи словаря request.POST только строки
        task.save()


def index(request):
    # данные для формсета, если уже были заполнены поля, то данные, которые были заполнены, сохранятся по ключу form-N-text 
    data = {
        'form-TOTAL_FORMS' : '2',
        'form-INITIAL_FORMS' : '0',
        'form-0-text' : '',
        'form-1-text' : '',
    }
    formset = formset_factory(FormTask, extra=2)

    t = ""

    if request.method == "POST":
        last_item = list(request.POST.keys())[-1]
        if 'new_panel' == last_item:
            # if request
            savePanel(request)
        if 'change' == last_item:
            t = changePanel(request)
        if 'del' == last_item:
            Panel.objects.get( id = request.POST[last_item]).delete()

        if 'add_field' == last_item:
            for key, item in request.POST.items(): #переименовать item <- задача для программиста, для тебя блять еблан
                if 'form' in key:
                    data[key] = item

            #минус crsf токен
            add = len(request.POST) - 1
            data['form-TOTAL_FORMS'] = str(add)
            formset = formset_factory(FormTask, extra=add) #перегружаем formset для количества add

    # form = FormTask()
    content = {
        'panels' : Panel.objects.all(),
        # 'form' : form,
        'formset' : formset(data),
        'g' : request.GET,
        'p' : request.POST,
        "t" : t if t else "not"
    }

    return render(request, "notes/index.html", content)


