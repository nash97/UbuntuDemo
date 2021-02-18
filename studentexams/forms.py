from django.forms import ModelForm
# models for which we want to create the form and save records into the DB
from studentexams.models import userRegistrationModel
from django import forms

class UserRegistrationForm(ModelForm):
    class Meta:
        model = userRegistrationModel    # from models.py
        fields = '__all__'          # fields to be shown into the html form

class UpdateUserRegistrationForm(ModelForm):
    class Meta:
        model = userRegistrationModel    # from models.py
        fields = [ "firstname", 'lastname', "username", "email", "password", "mobile"]          # fields to be shown into the html form

# class CustomerLoginForm(ModelForm):
#     class Meta:
#         model = UserRegistration    # from models.py
#         fields = [ "email", "password" ]
