# Generated by Django 2.1.1 on 2018-09-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_pic', models.ImageField(upload_to='')),
            ],
        ),
    ]
