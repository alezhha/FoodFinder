# Generated by Django 3.2.9 on 2021-11-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211104_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Легко'), ('Hard', 'Сложно'), ('Medium', 'Средне')], default='Легко', max_length=10, verbose_name='Сложность'),
        ),
    ]
