# Generated by Django 2.0.1 on 2018-03-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_site', '0002_auto_20180321_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]
