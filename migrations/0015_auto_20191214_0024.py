# Generated by Django 3.0 on 2019-12-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20191213_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='new',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='marks',
            name='count',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
