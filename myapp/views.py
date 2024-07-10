from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import MyModel


def hi(request):
    return HttpResponse("This is hi function", )

def hello(request):
    if request.method == "POST":
        xname = request.POST.get('uname')
        xage = request.POST.get('uage')
        data = MyModel(name = xname, age = xage)
        data.save()
        datas = MyModel.objects.all()
    else:
        datas = MyModel.objects.all()
    return render(request, 'basic.html', context = {"xyz": datas})

