# Generated by Django 3.1.7 on 2021-04-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210425_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobportal',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
