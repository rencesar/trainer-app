from django.db import models


class OurUser:
    cpf = models.CharField(verbose_name='CPF', max_length=11, null=False, blank=False)

