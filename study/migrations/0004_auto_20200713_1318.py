# Generated by Django 3.0.8 on 2020-07-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20200713_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=150, verbose_name='Отрывок'),
        ),
    ]
