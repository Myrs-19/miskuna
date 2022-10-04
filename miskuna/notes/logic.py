from .models import Task, Panel

import re

def save_panel(request):
    for key, item in request.POST.items():
        if key == 'form-0-text':
            p = Panel(title=item)
            p.save()
        elif "form" in key:
            t = Task(text=item, panel=p)
            t.save()


# post, change
def change_panel(request):

    tasks = [Task.objects.get(pk=key) for key, value in request.POST.items() if key.isnumeric()]

    # получаем панель которую будет изменять
    panel = Panel.objects.get(pk=request.POST['change']) # в request.POST['change'] хранится pk панели
    panel.title=request.POST['title']
    panel.save()

    # задачи которые нужно поменять
    for task in tasks:
        task.text = request.POST[str(task.pk)] #type(task.pk) - int, ключи словаря request.POST только строки
        task.save()


def del_task(pk):
    Task.objects.get(pk=pk).delete()


def get_key_for_del(request):
    '''
        возвращает ключ элемента (task's object), который нужно удалить
        возвращает пустую строку при отсутствии ключа (пользователь выбрал другое действие)
    '''

    l_key = [key for key in request.POST.keys() if re.search("del-\d", key)]
    return "".join(l_key) if l_key else ""