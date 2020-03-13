from django.db import models

class posts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100, default='Ausaf Liaquat')
    image = models.ImageField(upload_to='mywebapp/img/')
    date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    webs = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name