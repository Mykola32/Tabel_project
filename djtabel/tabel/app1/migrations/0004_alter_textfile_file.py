# Generated by Django 4.2.6 on 2023-11-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_textfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='file',
            field=models.FileField(null=True, upload_to='app1/', verbose_name='Текстовий файл'),
        ),
    ]