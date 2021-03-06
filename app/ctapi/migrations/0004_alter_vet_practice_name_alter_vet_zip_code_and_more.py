# Generated by Django 4.0 on 2021-12-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctapi', '0003_cat_medication_vet_vetvisit_vet_cats_prescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vet',
            name='practice_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vet',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='vet',
            unique_together={('vet_name', 'practice_name')},
        ),
    ]
