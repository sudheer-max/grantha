# Generated by Django 3.0.4 on 2020-03-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grantha', '0003_auto_20200322_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('car_name', models.CharField(max_length=100)),
                ('ac_rate', models.IntegerField(default=0)),
                ('extra_person', models.IntegerField(default=0)),
                ('extra_hr', models.IntegerField(default=0)),
                ('night_allowance', models.IntegerField(default=0)),
            ],
        ),
    ]
