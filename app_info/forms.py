from django import forms
from . models import StudentDetail, AcademicDetail, TrainingDetail

class StudentDetailForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # fieds = "__all__" -- to select all the fields
        fields = ("first_name", "middle_name", "last_name","contact", "email", "password") # This is for selective fields
        model = StudentDetail

class StudentLoginForm(forms.ModelForm):
    class Meta:
        fields=("email", "password")
        model = StudentDetail



class AcademicDetailForm(forms.ModelForm):
    class Meta:
        fields = ("org_name", "org_location", "academic_degree", "secured_marks")
        model = AcademicDetail   

class TrainingDetailForm(forms.ModelForm):
    class Meta:
        fields = ("org_name", "titile", "category", "duration")
        model = TrainingDetail