# Generated by Django 5.1.5 on 2025-05-22 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0004_cd_date_emprunt_cd_emprunteur_dvd_date_emprunt_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Emprunt',
        ),
    ]
