# Generated by Django 2.1.7 on 2021-04-05 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('desc', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]