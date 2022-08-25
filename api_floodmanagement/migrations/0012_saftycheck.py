# Generated by Django 3.2.13 on 2022-08-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_floodmanagement', '0011_alter_flooddataset_water_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaftyCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=19)),
            ],
        ),
    ]