# Generated by Django 4.2.3 on 2023-07-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acteur',
            name='satut',
        ),
        migrations.RemoveField(
            model_name='acteur',
            name='speudo',
        ),
        migrations.AddField(
            model_name='acteur',
            name='statut',
            field=models.CharField(choices=[('ADMINISTRATEUR', 'Administrateur'), ('CREATOR', 'Créateur'), ('USER', 'Abonné')], default='Abonné', max_length=30, verbose_name='statut'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habitant',
            name='typepiece',
            field=models.CharField(choices=[('HH', 'Cart National Identity'), ('EN', 'Extrait Naissance'), ('AI', 'Attestation Identity'), ('CE', 'Carte Etudiant'), ('Autre', 'Autre')], max_length=20),
        ),
        migrations.AlterField(
            model_name='referentielmetier',
            name='work_name',
            field=models.CharField(choices=[('Mecanicien', 'Mecanicien'), ('maçon', 'maçon'), ('menusier', 'menusier'), ('plombier', 'plombier'), ('etudiant', 'etudiant'), ('Autre', 'Autre')], max_length=20),
        ),
    ]
