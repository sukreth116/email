# Generated by Django 4.1 on 2022-12-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0010_agefactor_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agefactor_tb',
            name='maximum_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='agefactor_tb',
            name='minimum_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seasoncountry_tb',
            name='months',
            field=models.IntegerField(),
        ),
    ]
