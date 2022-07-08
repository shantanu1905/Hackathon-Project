# Generated by Django 3.2.13 on 2022-07-08 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_floodmanagement', '0004_auto_20220630_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhelprequest',
            name='RequestStatus',
            field=models.CharField(choices=[('HELP ALERT SEND TO AUTHORITIES', 'HELP ALERT SEND TO AUTHORITIES'), ('HELP TO YOUR LOCATION DEPLOYED', 'HELP TO YOUR LOCATION DEPLOYED'), ('OPERATION COMPLETED', 'OPERATION COMPLETED')], default='HELP ALERT SEND TO AUTHORITIES', max_length=30),
        ),
        migrations.CreateModel(
            name='CrowdSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
