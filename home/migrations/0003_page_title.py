# Generated by Django 2.0.4 on 2018-04-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180419_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
