# Generated by Django 4.0.4 on 2022-05-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coachees',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default=True, max_length=25)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('pic', models.FileField(blank=True, null=True, upload_to='media/')),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default=True, max_length=25)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('pic', models.FileField(blank=True, null=True, upload_to='media/')),
                ('password', models.CharField(blank=True, max_length=1024, null=True)),
                ('linked_in', models.CharField(blank=True, max_length=100, null=True)),
                ('charge', models.CharField(blank=True, max_length=100, null=True)),
                ('certi', models.CharField(blank=True, choices=[(1, 'ICF ACC'), (2, 'ICF PCC'), (3, 'ICF MCC')], max_length=2, null=True)),
            ],
        ),
    ]
