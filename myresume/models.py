from django.db import models


# Create your models here.

class Technical(models.Model):
    tech_name = models.CharField(max_length=200)
    tech_description = models.TextField(null=True)
    script_code = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ["tech_name", "tech_description", "script_code"]

    def __str__(self):
        return self.tech_name


class Resume(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    story = models.TextField()
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='resume-images', null=True)
    work_exp = models.FloatField(default=0.0, null=True)
    part_project = models.IntegerField(default=0, null=True)
    university = models.CharField(max_length=200, null=True)
    gpa = models.FloatField(null=True)
    linked = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ['name', 'birthday', 'phone', 'address', 'email', 'story', 'position']

    def __str__(self):
        return self.name


class DetailTechnical(models.Model):
    tech_name = models.ForeignKey(Technical, on_delete=models.CASCADE)
    name = models.ForeignKey(Resume, on_delete=models.CASCADE)
    tech_exp = models.FloatField(null=True, default=0.0)
    tech_level = models.IntegerField()

    class Meta:
        ordering = ["id"]


class OtherImage(models.Model):
    image = models.ImageField(upload_to='resume-image')
    name = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_des = models.TextField()
    company_img = models.ImageField(upload_to='resume-image', null=True)

    def __str__(self):
        return self.company_name


class CompaniesWorked(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_exp = models.FloatField(default=0)
    name = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    name = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_des = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='resume-image')

    def __str__(self):
        return self.project_name
