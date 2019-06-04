from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.contrib.auth.models import User

class StudentSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'Email'}), max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    birthdate = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Birth Date'}), initial=datetime.date.today)
    skills = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Skills'}))

    class Meta(UserCreationForm.Meta):
        #model = models.Student
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email', 'birthdate', 'skills')

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(username=data['username'], email=data['email'], first_name=data['first_name'],
                    last_name=data['last_name'], password=data['password1'],
                     is_staff=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        student = models.Student(user=user, birth_date=data['birthdate'],
                          skills=data['skills'])
        student.save()


class BussinessSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    company_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Company Name'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'Email'}), max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    projects = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Company Projects:'}))
    begin_date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Creation Date'}), initial=datetime.date.today)

    class Meta(UserCreationForm.Meta):
        
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + \
            ('company_name', 'email', 'projects', 'begin_date')

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'],is_staff=True)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        business = models.Business(user=user, company_name=data['company_name'],
                                   projects=data['projects'], begin_date=data['begin_date'])
        business.save()

class CourseContentForm(forms.ModelForm):
    class Meta:
        model = models.CourseMaterials
        fields = '__all__'
        exclude = ['course']
    # def save(self):
    #     data = self.cleaned_data
    #     print(data)
    #     materials = models.CourseMaterials(course=self.course, **data)
    #     materials.save()