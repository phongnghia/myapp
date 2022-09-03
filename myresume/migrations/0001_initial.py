# Generated by Django 4.1 on 2022-09-03 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('story', models.TextField()),
                ('position', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name', 'birthday', 'phone', 'address', 'email', 'story', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=200)),
                ('tech_description', models.TextField(null=True)),
            ],
            options={
                'ordering': ['tech_name'],
            },
        ),
        migrations.CreateModel(
            name='DetailTechnical',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('tech_exp', models.FloatField()),
                ('tech_level', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresume.resume')),
                ('tech_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myresume.technical')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
