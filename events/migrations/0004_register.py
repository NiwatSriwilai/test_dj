# Generated by Django 2.1.1 on 2018-09-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
    ]