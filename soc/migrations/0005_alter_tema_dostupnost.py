# Generated by Django 4.2.13 on 2024-05-31 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0004_alter_dostupnost_nazov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='dostupnost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='soc.dostupnost'),
        ),
    ]
