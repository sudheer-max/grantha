# Generated by Django 3.0.4 on 2020-03-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grantha', '0004_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(default='this is text aboutus writeup')),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
