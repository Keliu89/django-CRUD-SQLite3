# Generated by Django 4.0.5 on 2022-06-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
    ]