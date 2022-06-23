from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url, redirect

from quiz.forms import *
from quiz.models import *


class SelectExamFormView(LoginRequiredMixin, generic.FormView):
    login_url = 'login'
    template_name = 'home.html'
    form_class = SelectExamForm
    success_url = 'thanks'

    def form_valid(self, form):
        selected = form.cleaned_data.get("exams")
        return redirect('question_list', exam_id=selected.id)

    def get_context_data(self, **kwargs):
        context = super(SelectExamFormView, self).get_context_data(**kwargs)
        context['submitted_exams'] = self.request.user.exams.all()
        context['button_name'] = 'start'
        return context


class QuestionListView(LoginRequiredMixin, generic.RedirectView):
    login_url = 'login'

    def get_redirect_url(self, *args, **kwargs):
        """
        Return the URL redirect to. Keyword arguments from the URL pattern
        match generating the redirect request are provided as kwargs to this
        method.
        """
        print(self.kwargs['exam_id'], 'exam_id')
        exam_id=self.kwargs['exam_id']
        q = Question.objects.filter(exam_id=exam_id).first()
        print(resolve_url('question', exam_id=exam_id, question_id=q.id), 'resolve')
        return resolve_url('question', exam_id=exam_id, question_id=q.id)


class QuestionFormView(LoginRequiredMixin, FormMixin, generic.DetailView):
    login_url = 'login'
    template_name = 'home.html'
    form_class = QuestionForm
    model = Question
    pk_url_kwarg = "question_id"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(exam_id=self.kwargs['exam_id'])

    def get_context_data(self, **kwargs):
        context = super(QuestionFormView, self).get_context_data(**kwargs)
        context.update({"question_list": self.get_queryset()})
        context['button_name'] = 'submit'
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"question": self.object})
        return kwargs
