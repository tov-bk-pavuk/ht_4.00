#  from django.http import HttpResponse
from django.shortcuts import render

from .forms import Triangle

'''
def index(request):
    return HttpResponse("<p>Аллиуйа, Аминь. Надо было убрать скобки после переменной  "
                        "views.index в файле urls.py </p>")

def title(request):
    return HttpResponse('<h2>Страница треугольника</h2>')
'''


def index(request):
    side_a = 4
    side_b = 4
    tri_type = ['прямоугольный', 'равносторонний', 'равнобедренный']
    form = Triangle()
    tt = str()
    if side_a == side_b:
        tt = tri_type[2]
    else:
        tt = tri_type[0]
    data = {'text': 'Добрый вечер', 'side_a': side_a,
            'side_b': side_b, 'tri_type': tt, 'tr_form': form}
    return render(request, 'index.html', context=data)
