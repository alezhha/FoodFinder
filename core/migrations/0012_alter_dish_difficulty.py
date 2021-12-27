# Generated by Django 3.2.9 on 2021-11-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_dish_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Легко'), ('Medium', 'Средне'), ('Hard', 'Сложно')], default='Легко', max_length=10, verbose_name='Сложность'),
        ),
    ]
