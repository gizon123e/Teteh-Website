# Generated by Django 4.2.1 on 2023-05-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filosofi_pendidikan_indonesia', '0004_text_materi_pertama'),
    ]

    operations = [
        migrations.CreateModel(
            name='text_materi_kedua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_materi_2', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='text_materi_ketiga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_materi_3', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
