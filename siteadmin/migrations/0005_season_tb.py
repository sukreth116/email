# Generated by Django 4.1 on 2022-12-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0004_hobbyfactor_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='season_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=20)),
            ],
        ),
    ]
