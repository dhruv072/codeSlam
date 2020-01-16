# Generated by Django 2.2.1 on 2019-10-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20)),
                ('Date', models.DateField()),
                ('Open', models.IntegerField()),
                ('High', models.IntegerField()),
                ('Low', models.IntegerField()),
                ('Close', models.IntegerField()),
                ('Volume', models.IntegerField()),
                ('AdjustmentFactor', models.IntegerField()),
                ('AdjustmentType', models.IntegerField()),
                ('avgvolume', models.IntegerField()),
            ],
            options={
                'ordering': ('avgvolume',),
            },
        ),
    ]
