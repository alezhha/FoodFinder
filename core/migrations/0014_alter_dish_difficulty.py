# Generated by Django 3.2.9 on 2021-11-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20211106_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Легко'), ('Hard', 'Сложно'), ('Medium', 'Средне')], default='Легко', max_length=10, verbose_name='Сложность'),
        ),
    ]
