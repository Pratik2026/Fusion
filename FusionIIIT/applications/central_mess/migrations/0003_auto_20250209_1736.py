# Generated by Django 3.1.5 on 2025-02-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0002_auto_20241012_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_request',
            name='img',
            field=models.ImageField(default=None, upload_to='mess/images/registration_request/%Y/%m/%d/'),
        ),
    ]
