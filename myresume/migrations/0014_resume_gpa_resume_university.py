# Generated by Django 4.1 on 2022-09-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0013_resume_part_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='gpa',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='university',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
