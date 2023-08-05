# Generated by Django 4.2.3 on 2023-08-01 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_alter_acteur_habitantid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carnetsante',
            old_name='end_date',
            new_name='date_recorder',
        ),
        migrations.RemoveField(
            model_name='carnetsante',
            name='start_date',
        ),
        migrations.AddField(
            model_name='carnetsante',
            name='temperature',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='carnetsante',
            name='acteurID',
        ),
        migrations.AddField(
            model_name='carnetsante',
            name='acteurID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient', to='exchange.habitant'),
        ),
    ]