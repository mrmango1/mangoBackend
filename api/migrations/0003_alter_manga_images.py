# Generated by Django 4.0.6 on 2022-08-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_mangas_manga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='images',
            field=models.ImageField(upload_to='api/manga'),
        ),
    ]
