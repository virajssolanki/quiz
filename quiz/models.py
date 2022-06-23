from django.db import models


class Exam(models.Model):
    name = models.CharField(verbose_name='name', max_length=256, blank=True, null=True)
    submitted_by = models.ManyToManyField('account.User', related_name='exams', blank=True)  

    class Meta:
        db_table = 'exam'

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    exam = models.ForeignKey('quiz.Exam', related_name='qustions', on_delete=models.CASCADE, blank=True, null=True)
    question = models.CharField(verbose_name='qustion', max_length=256, blank=True, null=True)
    answer = models.CharField(verbose_name='answer', max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return str(self.question)


class Answer(models.Model):
    question = models.ForeignKey('quiz.Question', related_name='mcqs', on_delete=models.CASCADE, blank=True, null=True)
    option = models.CharField(verbose_name='option', max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return str(self.option)