# Generated by Django 4.1.3 on 2022-11-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='breed',
            new_name='bird_family',
        ),
        migrations.RenameField(
            model_name='finch',
            old_name='description',
            new_name='key_information',
        ),
        migrations.RenameField(
            model_name='finch',
            old_name='name',
            new_name='scientific_name',
        ),
        migrations.RenameField(
            model_name='finch',
            old_name='age',
            new_name='weight',
        ),
        migrations.AddField(
            model_name='finch',
            name='food',
            field=models.CharField(default='food', max_length=100),
            preserve_default=False,
        ),
    ]
