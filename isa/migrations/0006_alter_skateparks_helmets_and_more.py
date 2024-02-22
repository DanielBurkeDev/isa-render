# Generated by Django 4.2.6 on 2023-11-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isa', '0005_skateparks_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skateparks',
            name='helmets',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10),
        ),
        migrations.AlterField(
            model_name='skateparks',
            name='indooroutdoor',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'), ('Unknown', 'Unknown')], max_length=20),
        ),
        migrations.AlterField(
            model_name='skateparks',
            name='lights',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10),
        ),
        migrations.AlterField(
            model_name='skateparks',
            name='surface',
            field=models.CharField(choices=[('Concrete', 'Concrete'), ('WOWoodOD', 'Wood'), ('Unknown', 'Unknown')], max_length=20),
        ),
    ]