# Generated by Django 5.1.4 on 2025-01-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0006_doctor_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='clinic_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='contact_info',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
