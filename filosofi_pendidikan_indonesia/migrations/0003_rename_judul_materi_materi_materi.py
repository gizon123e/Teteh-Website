# Generated by Django 4.2.1 on 2023-05-29 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filosofi_pendidikan_indonesia', '0002_rename_materi_materi_judul_materi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materi',
            old_name='judul_materi',
            new_name='materi',
        ),
    ]