# Generated by Django 4.1.3 on 2022-11-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='webapp.photos', verbose_name='Избранные'),
        ),
    ]