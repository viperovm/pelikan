# Generated by Django 3.0.8 on 2020-07-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at', 'title'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='is_pulished',
            new_name='is_published',
        ),
    ]