from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    form_type = models.CharField(max_length=20)  # 'signin' ya 'login'

    def _str_(self):
        return self.email


# Create your models here.
