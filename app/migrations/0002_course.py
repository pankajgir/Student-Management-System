# Generated by Django 5.0.4 on 2024-05-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('fees', models.IntegerField(max_length=250)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]
