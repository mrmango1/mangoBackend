# Generated by Django 4.0.6 on 2022-08-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_manga_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='images',
            field=models.ImageField(upload_to='api/images/manga'),
        ),
    ]
