# Generated by Django 2.1.7 on 2019-03-17 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_course_note_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='note_slug',
        ),
    ]
