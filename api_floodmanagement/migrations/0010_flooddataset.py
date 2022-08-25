# Generated by Django 3.2.13 on 2022-08-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_floodmanagement', '0009_auto_20220825_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloodDataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Site_Name', models.CharField(max_length=20)),
                ('River', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('District', models.CharField(max_length=20)),
                ('water_level', models.DecimalField(decimal_places=3, max_digits=5)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=19)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
