# Generated by Django 2.1 on 2018-10-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_auto_20181001_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(default='', max_length=31, unique=True),
        ),
    ]