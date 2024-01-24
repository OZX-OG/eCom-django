# forms.py
from django import forms
from .models import Task

class OrderStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'Select Status'),
        ("Pending", "Pending"),
        ("Processed", "Processed"),
        ("Closed", "Closed"),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-3'}))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
            self.fields['user'].widget.attrs['readonly'] = True
            self.fields['user'].widget.attrs['disabled'] = True