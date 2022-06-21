from django.db import models


class Exam(models.Model):
    name = models.CharField(verbose_name='name', max_length=256, blank=True, null=True)
    submitted_by = models.ManyToManyField('account.User', related_name='exams', blank=True)  

    class Meta:
        db_table = 'exam'

    def __str__(self):
        return str(self.name)


class Qustion(models.Model):
    exam = models.ForeignKey('quiz.Exam', related_name='mcqs', on_delete=models.CASCADE, blank=True, null=True)
    qustion = models.CharField(verbose_name='qustion', max_length=256, blank=True, null=True)
    answer = models.CharField(verbose_name='answer', max_length=256, blank=True, null=True)
    option_a = models.CharField(verbose_name='a', max_length=256, blank=True, null=True)
    option_b = models.CharField(verbose_name='b', max_length=256, blank=True, null=True)    
    option_c = models.CharField(verbose_name='c', max_length=256, blank=True, null=True)    
    option_d = models.CharField(verbose_name='d', max_length=256, blank=True, null=True)    


    class Meta:
        db_table = 'qustion'

    def __str__(self):
        return str(self.qustion)
