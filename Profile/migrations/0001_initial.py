# Generated by Django 4.2.2 on 2023-07-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndiviadualUserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]