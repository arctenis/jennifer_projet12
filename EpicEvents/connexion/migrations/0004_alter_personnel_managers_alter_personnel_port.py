# Generated by Django 4.1.6 on 2023-02-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0003_auto_20230213_1654'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='personnel',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='personnel',
            name='port',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
