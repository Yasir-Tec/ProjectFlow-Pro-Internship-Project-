# Generated by Django 3.0 on 2019-12-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_auto_20191225_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restype', models.CharField(default=True, max_length=100)),
                ('resqua', models.IntegerField(default=True)),
            ],
        ),
    ]
