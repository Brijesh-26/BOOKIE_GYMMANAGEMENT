# Generated by Django 4.1.7 on 2023-12-14 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_workoutsession_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutsession',
            name='date',
            field=models.DateField(),
        ),
    ]
