# Generated by Django 3.2.8 on 2021-10-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapi', '0002_auto_20211022_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='score',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
