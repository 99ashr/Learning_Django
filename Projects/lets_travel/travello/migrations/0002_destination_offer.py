# Generated by Django 3.1.5 on 2021-01-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
