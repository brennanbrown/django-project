# Generated by Django 3.0.3 on 2020-08-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(default='TITLE', max_length=128)),
                ('summary', models.CharField(default='SUMMARY', max_length=256)),
                ('date', models.CharField(default='DATE', max_length=128)),
                ('hyperlink', models.CharField(default='HYPERLINK', max_length=256)),
            ],
        ),
    ]
