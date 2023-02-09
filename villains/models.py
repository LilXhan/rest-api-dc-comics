from django.db import models

class Villain(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name 

    class Meta:
        db_table = 'villains'