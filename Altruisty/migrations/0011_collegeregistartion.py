# Generated by Django 5.1.4 on 2024-12-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Altruisty', '0010_user_detail_userauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='collegeRegistartion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=30, null=True)),
                ('Name', models.CharField(max_length=50)),
                ('contact_email', models.CharField(max_length=50)),
                ('contact_phonenumber', models.CharField(max_length=15)),
                ('College_name', models.CharField(max_length=50)),
                ('Address_line_1', models.CharField(max_length=30)),
                ('Area', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('zipcode', models.CharField(max_length=6)),
                ('status', models.CharField(blank=True, max_length=300, null=True)),
                ('ep1', models.CharField(blank=True, max_length=300, null=True)),
                ('ep2', models.CharField(blank=True, max_length=300, null=True)),
                ('ep3', models.CharField(blank=True, max_length=300, null=True)),
                ('ep4', models.CharField(blank=True, max_length=300, null=True)),
                ('ep5', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'College_Registartion',
            },
        ),
    ]
