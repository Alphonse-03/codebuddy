# Generated by Django 3.1.7 on 2021-04-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210422_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='sender',
            field=models.BooleanField(default=True),
        ),
    ]
