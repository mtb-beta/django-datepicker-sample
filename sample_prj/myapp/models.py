from django.db import models
from django.utils import timezone

class MyModel(models.Model):
    input_date = models.DateField("日付を入れます", default=timezone.now)

    def __str__(self):
        return self.input_date
