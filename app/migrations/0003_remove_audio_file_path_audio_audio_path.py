# Generated by Django 4.2.1 on 2023-06-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book_pdf_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='file_path',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_path',
            field=models.FileField(default=None, upload_to='audios/'),
            preserve_default=False,
        ),
    ]