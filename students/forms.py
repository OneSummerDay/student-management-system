from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'students_number',
            'first_name',
            'last_name',
            'email',
            'fields_of_study',
            'gpa',
        ]
        labels = {
            'students_number': 'Номер учня',
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'email': 'Email',
            'fields_of_study': 'Спеціальність',
            'gpa': 'Середній бал',
        }
        widgets = {
            'students_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fields_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

