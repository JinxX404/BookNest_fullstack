# Generated by Django 5.1.2 on 2025-06-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books', to='books.genre'),
        ),
        migrations.DeleteModel(
            name='BookGenre',
        ),
    ]
