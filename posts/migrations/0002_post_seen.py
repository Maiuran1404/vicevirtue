# Generated by Django 3.0.7 on 2020-06-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seen',
            field=models.CharField(default='00000', editable=False, max_length=5),
        ),
    ]
