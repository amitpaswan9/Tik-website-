# Generated by Django 2.1 on 2018-10-02 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments',
            new_name='comment_text',
        ),
    ]
