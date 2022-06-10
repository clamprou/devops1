# Generated by Django 3.0 on 2022-06-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Aproved'), ('2', 'Dissaproved'), ('3', 'Pending')], default='Pending', max_length=30)),
            ],
        ),
    ]
