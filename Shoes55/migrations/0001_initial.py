# Generated by Django 4.2.1 on 2023-06-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('uemail', models.EmailField(max_length=30)),
                ('upasswd', models.CharField(max_length=30)),
            ],
        ),
    ]
