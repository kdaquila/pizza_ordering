# Generated by Django 4.0 on 2021-12-24 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(null=True)),
                ('stop_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'pizza',
            },
        ),
    ]
