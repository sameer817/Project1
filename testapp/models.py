from django.db import models
from django.urls import reverse

class ContactModel(models.Model):
    first_name = models.CharField('First Name', max_length = 25)
    last_name = models.CharField('Last Name', max_length = 25)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.last_name

class EmailModel(models.Model):
    name = models.CharField(max_length = 25, default = '')
    From = models.EmailField()
    To = models.EmailField()
    Subject = models.CharField(max_length = 50)
    Message = models.TextField()

    def __str__(self):
        return self.Subject

# class SignupModel(models.Model):
#     username = models.CharField(max_length = 25)
#     password = models.CharField(max_length = 30)
#     email = models.EmailField()
#     first_name = models.CharField(max_length = 25)
#     last_name = models.CharField(max_length = 25)

class GenerateTextmodel(models.Model):
    Name = models.CharField(max_length = 20)
    Text = models.TextField()

    def get_absolute_url(self):
        return reverse('TextView',)
