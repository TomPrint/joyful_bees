from django.db import models

# Create your models here.

class NewsletterUser (models.Model):
    email= models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class MailMessage (models.Model):
    title = models.CharField (max_length=100, null=True)
    message = models.TextField(max_length = 400)

    def __str__(self):
        return self.title

    