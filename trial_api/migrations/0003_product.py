# Generated by Django 4.1.2 on 2022-11-14 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial_api', '0002_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('in_stocks', models.BooleanField(default=True)),
            ],
        ),
    ]