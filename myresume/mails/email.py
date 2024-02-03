from django.db import models


class EmailMyresume(models.Model):
    your_name = models.CharField(max_length=200)
    your_email = models.TextField(null=True)
    email_subject = models.CharField(max_length=200, null=True)
    email_description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.your_name
