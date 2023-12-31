# Generated by Django 4.2.6 on 2023-11-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0013_auto_20231124_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableEight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload_faculty', models.CharField(max_length=50)),
                ('workload_semester', models.CharField(max_length=50)),
                ('workload_course', models.CharField(max_length=50)),
                ('workload_types', models.CharField(max_length=100)),
                ('workload_duties', models.CharField(max_length=100)),
                ('workload_total', models.IntegerField(default=0)),
            ],
        ),
    ]
