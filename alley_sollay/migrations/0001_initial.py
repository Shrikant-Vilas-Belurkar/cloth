# Generated by Django 4.2.9 on 2024-02-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Black',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tshirt', models.CharField(max_length=25)),
                ('Size', models.CharField(max_length=25)),
                ('Color', models.CharField(max_length=25)),
            ],
        ),
    ]
