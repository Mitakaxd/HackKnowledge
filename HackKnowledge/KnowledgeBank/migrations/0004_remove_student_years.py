# Generated by Django 2.2.1 on 2019-06-02 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBank', '0003_auto_20190602_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='years',
        ),
    ]
