# Generated by Django 3.2.9 on 2021-11-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_dish_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='difficulty',
            field=models.CharField(choices=[('Hard', 'Сложно'), ('Medium', 'Средне'), ('Easy', 'Легко')], default='Легко', max_length=10, verbose_name='Сложность'),
        ),
        migrations.RemoveField(
            model_name='dish',
            name='products',
        ),
        migrations.AddField(
            model_name='dish',
            name='products',
            field=models.ManyToManyField(to='core.Product'),
        ),
    ]
