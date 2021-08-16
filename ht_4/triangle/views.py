from django.http import HttpResponse


def index(request):
    return HttpResponse("Аллиуйа, Аминь. Я так и не понял, что было не так. "
                        "Похоже, что порядок URL перечисленный в файле urls.py "
                        "папки проекта имел значение.")
