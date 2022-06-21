from django import forms

from quiz.models import Exam


class SelectExamForm(forms.Form):
    exams = forms.ModelChoiceField(queryset=Exam.objects.all())