# Generated by Django 5.0.2 on 2024-03-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=10)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Place', models.CharField(max_length=10)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]
