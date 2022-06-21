from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from quiz.forms import SelectExamForm
from quiz.models import *


class SelectExamFormView(LoginRequiredMixin, generic.FormView):
    login_url = 'login'
    template_name = 'home.html'
    form_class = SelectExamForm
    success_url = 'thanks'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SelectExamFormView, self).get_context_data(**kwargs)
        context['submitted_exams'] = self.request.user.exams.all()
        return context
    

class QustionView(LoginRequiredMixin, generic.ListView):
    model = Qustion
    template_name = 'qustion.html'
    context_object_name = "object_list"   
    paginate_by = 5 

    def get_queryset(self, *args, **kwargs):
        qs = super(QustionView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs
