from django.db import models


# Create your models here.

class My_technical(models.Model):
    tech_name = models.CharField(max_length=200)
    tech_description = models.TextField(null=True)

    class Meta:
        ordering = ["tech_name"]

    def __str__(self):
        return self.tech_name


class My_resume(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    story = models.TextField()
    position = models.CharField(max_length=200)

    class Meta:
        ordering = ['name', 'birthday', 'phone', 'address', 'email', 'story', 'position']

    def __str__(self):
        return self.name


class Detail_technical(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    tech_name = models.ForeignKey(My_technical, on_delete=models.CASCADE)
    name = models.ForeignKey(My_resume, on_delete=models.CASCADE)
    tech_exp = models.FloatField()
    tech_level = models.IntegerField()

    class Meta:
        ordering = ["id"]

    def __int__(self):
        return self.id
