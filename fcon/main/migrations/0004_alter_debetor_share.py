# Generated by Django 4.0.5 on 2022-07-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_person_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debetor',
            name='share',
            field=models.FloatField(null=True),
        ),
    ]
