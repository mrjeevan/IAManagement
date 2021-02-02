from django import forms
from .models import *

class AddStudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'

class AddSemsecForm(forms.ModelForm):
    class Meta():
        model = SemSec
        fields = '__all__'

class AddSubjectForm(forms.ModelForm):
    class Meta():
        model = Subject
        fields = '__all__'

class AddmarksForm(forms.ModelForm):
    class Meta():
        model = IAmark
        fields = '__all__'

class AddFacultyForm(forms.ModelForm):
    class Meta():
        model = Faculty
        fields = '__all__'

class AddInchargeForm(forms.ModelForm):
    class Meta():
        model = Incharge
        fields = '__all__'