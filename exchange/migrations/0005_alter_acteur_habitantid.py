# Generated by Django 4.2.3 on 2023-07-31 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_alter_habitant_work_space'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acteur',
            name='HabitantID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='utilisateur', to='exchange.habitant'),
        ),
    ]
