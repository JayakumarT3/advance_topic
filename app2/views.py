from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Register

def formfunc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        DOB = request.POST.get('dob')
        password = request.POST.get('password')
        Register.objects.create(name = name, email = email, dob = DOB, password = password)
        return redirect('basic')

    else:
        xform = MyForm()
    return render(request, 'form.html', context= {'form' : xform})
