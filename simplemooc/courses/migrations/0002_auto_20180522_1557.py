# Generated by Django 2.0 on 2018-05-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='couses/images', verbose_name='Imagem'),
        ),
    ]
