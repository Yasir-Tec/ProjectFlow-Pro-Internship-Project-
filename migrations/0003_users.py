# Generated by Django 3.0 on 2019-12-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_customuser_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(default='null', max_length=50, null=True)),
                ('select_dept', models.CharField(choices=[('cse', 'CSE'), ('mech', 'MECH'), ('civil', 'CIVIL'), ('auto', 'AUTO')], default='CSE', max_length=40)),
                ('email', models.EmailField(default=False, max_length=50)),
                ('contact', models.IntegerField(default=1234, max_length=30)),
            ],
        ),
    ]
