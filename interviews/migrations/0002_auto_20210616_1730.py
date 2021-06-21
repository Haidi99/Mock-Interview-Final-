# Generated by Django 3.2.4 on 2021-06-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=1000)),
                ('compare_text', models.TextField(blank=True, max_length=1000)),
                ('question_period', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='interview',
            name='compare_text',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='question',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='question_period',
        ),
    ]