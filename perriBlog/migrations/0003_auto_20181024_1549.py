# Generated by Django 2.0.9 on 2018-10-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perriBlog', '0002_auto_20181024_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perro',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]