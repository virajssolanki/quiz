from django.urls import path
 
from quiz.views import *


urlpatterns = [
    path('', SelectExamFormView.as_view(), name="home"),
    path('<exam_id>/', QuestionListView.as_view(), name='question_list'),
    path('<exam_id>/question/<question_id>/', QuestionFormView.as_view(), name='question'),

]
