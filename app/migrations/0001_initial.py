# Generated by Django 4.0.2 on 2022-02-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='Toyota', max_length=1000)),
                ('speed', models.IntegerField(default=120)),
                ('color', models.CharField(default='red', max_length=15)),
            ],
        ),
    ]
