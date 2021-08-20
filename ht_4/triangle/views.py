import math

from django.http import HttpResponse
from django.shortcuts import render


from .forms import Triangle


def index(request):
    if request.method == 'POST':
        s_1 = int(request.POST.get('side_1'))
        s_2 = int(request.POST.get('side_2'))
        result = math.sqrt(s_2*s_2+s_1*s_1)
        return HttpResponse(f'Гипотенуза = {result}')
    form = Triangle()
    data = {'tr_form': form}
    return render(request, 'index.html', context=data)
