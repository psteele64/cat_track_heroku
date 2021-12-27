# Generated by Django 4.0 on 2021-12-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=100)),
                ('email', models.EmailField(default='change_this_email@nowhere.com', max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'fosters',
            },
        ),
    ]
