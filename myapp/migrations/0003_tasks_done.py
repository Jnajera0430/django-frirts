# Generated by Django 4.1.7 on 2023-02-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
