# Generated by Django 3.1.5 on 2025-02-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=20)),
                ('remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='announcements',
            name='upload_announcement',
            field=models.FileField(default=None, null=True, upload_to='department/upload_announcement'),
        ),
    ]
