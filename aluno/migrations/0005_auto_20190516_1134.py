# Generated by Django 2.2.1 on 2019-05-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0004_auto_20190512_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='aluno/images/', verbose_name='Foto'),
        ),
    ]
