# Generated by Django 3.1.2 on 2020-10-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainprocess', '0002_auto_20201028_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='intrest',
            field=models.CharField(choices=[('C', 'C'), ('C++', 'C++'), ('Java', 'Java'), ('Python', 'Python')], max_length=6, null=True),
        ),
    ]