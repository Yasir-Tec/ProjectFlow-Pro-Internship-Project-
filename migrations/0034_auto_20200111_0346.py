# Generated by Django 3.0 on 2020-01-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0033_guide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name1',
            new_name='fname1',
        ),
        migrations.AddField(
            model_name='users',
            name='lname1',
            field=models.CharField(max_length=20, null=True),
        ),
    ]