# Generated by Django 4.2.5 on 2023-09-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0003_user_firstname_user_lastname_user_middlename'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
