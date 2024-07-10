from django import forms
from .models import Register

# class MyForm(forms.Form):
#     name = forms.CharField(label="Enter Your Name :", max_length=30)
#     email = forms.EmailField(label="Enter Your Email :")
#     dob = forms.DateField(label="Enter Your DOB :")
#     password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class MyForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'