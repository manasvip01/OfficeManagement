# Generated by Django 4.0.1 on 2022-01-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
