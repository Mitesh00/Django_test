# Generated by Django 4.0.4 on 2022-04-29 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educator_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educator_name', models.CharField(max_length=100)),
                ('courses_offer', models.CharField(max_length=100)),
            ],
        ),
    ]
