# Generated by Django 2.0.9 on 2018-10-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perriBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=200)),
                ('FechaNac', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Raza', models.CharField(max_length=200)),
                ('Descripcion', models.TextField(max_length=200)),
                ('Estado', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
