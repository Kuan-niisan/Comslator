# Generated by Django 5.0.7 on 2024-08-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('birth_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=None)),
                ('status', models.CharField(choices=[('online', 'on_line'), ('offline', 'off_line')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
