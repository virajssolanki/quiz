from django import forms
from django.forms.widgets import RadioSelect

from quiz.models import Exam, Question, Answer


class SelectExamForm(forms.Form):
    exams = forms.ModelChoiceField(queryset=Exam.objects.all())


# class QustionForm(forms.Form):
#     exams = forms.ModelChoiceField(
#         widget = RadioSelect, queryset=Answer.objects.all()
#     )


class QuestionForm(forms.Form):
    '''
    create dynamic form for each qustion
    '''
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        self.fields["option"] = forms.ModelChoiceField(
            queryset=question.mcqs.all(), 
            widget=RadioSelect, 
            label=question.question
        )