from django import forms
from student.models import Students

class studentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"