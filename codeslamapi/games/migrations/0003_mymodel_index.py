# Generated by Django 2.2.1 on 2019-10-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
