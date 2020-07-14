from django import forms
from .models import Question, Review


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['email', 'name', 'content']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'md-textarea form-control', 'rows': 2}),
        }
