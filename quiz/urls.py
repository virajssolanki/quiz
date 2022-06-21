from django.urls import path
 
from quiz.views import *


urlpatterns = [
    path('', SelectExamFormView.as_view(), name="home"),
    path('qustion/', QustionView.as_view(), name="qustion"),
    
]
