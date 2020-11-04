# Generated by Django 3.1.3 on 2020-11-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
            ],
        ),
    ]