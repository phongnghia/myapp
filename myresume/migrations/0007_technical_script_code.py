# Generated by Django 4.1 on 2022-09-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0006_alter_companiesworked_company_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='technical',
            name='script_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
