# Generated by Django 3.1.7 on 2021-04-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_doomsdaycountdowntimer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doomsdaycountdowntimer',
            name='duration_in_minutes',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doomsdaycountdowntimer',
            name='state',
            field=models.CharField(max_length=30),
        ),
    ]
