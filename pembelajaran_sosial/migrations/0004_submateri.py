# Generated by Django 4.2.1 on 2023-05-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembelajaran_sosial', '0003_remove_materi_sub_materi'),
    ]

    operations = [
        migrations.CreateModel(
            name='subMateri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subMateri_1', models.TextField(blank=True, default='', null=True)),
                ('subMateri_2', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]