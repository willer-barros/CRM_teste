import datetime
from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False)
    celular = models.CharField(max_length=11, null=False)
    pub_date = models.DateTimeField('Date publicada')

    def __str__(self):
        return self.nome
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)