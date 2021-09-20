# Generated by Django 3.2.7 on 2021-09-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('email', models.CharField(default='', max_length=100)),
                ('zip_code', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
