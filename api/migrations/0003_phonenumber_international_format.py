# Generated by Django 4.2.4 on 2023-09-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='international_format',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
