# Generated by Django 3.2.8 on 2021-10-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domanda',
            name='categoria',
            field=models.CharField(max_length=40, null=True),
        ),
    ]