# Generated by Django 3.1.5 on 2024-04-27 23:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('fine', models.IntegerField(default=0)),
                ('doc_count', models.IntegerField(default=0)),
                ('patho_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('doctor_phone', models.CharField(max_length=15)),
                ('specialization', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='medical_relief',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='medical_files/')),
                ('file_id', models.IntegerField(default=0)),
                ('compounder_forward_flag', models.BooleanField(default=False)),
                ('acc_admin_forward_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pathologist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pathologist_name', models.CharField(max_length=50)),
                ('pathologist_phone', models.CharField(max_length=15)),
                ('specialization', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('threshold', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(default=datetime.date.today)),
                ('brief', models.CharField(default='--', max_length=20)),
                ('request_details', models.CharField(max_length=200)),
                ('upload_request', models.FileField(blank=True, upload_to='')),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('remarks', models.CharField(default='--', max_length=300)),
                ('request_receiver', models.CharField(default='--', max_length=30)),
                ('request_ann_maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_requests_made', to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('test', models.CharField(blank=True, max_length=200, null=True)),
                ('file_id', models.IntegerField(default=0)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Prescribed_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.stock')),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Pathologist_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=10)),
                ('from_time', models.TimeField(blank=True, null=True)),
                ('to_time', models.TimeField(blank=True, null=True)),
                ('room', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('pathologist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.pathologist')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.stock')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_admit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_doctor', models.CharField(max_length=100)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(max_length=50)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.doctor')),
                ('hospital_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.hospital')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Expiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('supplier', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
                ('returned', models.BooleanField(default=False)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Doctors_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=10)),
                ('from_time', models.TimeField(blank=True, null=True)),
                ('to_time', models.TimeField(blank=True, null=True)),
                ('room', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100, null=True)),
                ('complaint', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.doctor')),
                ('schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.doctors_schedule')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ann_date', models.DateTimeField(default='04-04-2021')),
                ('message', models.CharField(max_length=200)),
                ('upload_announcement', models.FileField(default=' ', null=True, upload_to='health_center/upload_announcement')),
                ('anno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements_made', to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='Ambulance_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
    ]
