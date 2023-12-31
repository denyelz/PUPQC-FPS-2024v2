# Generated by Django 4.2.6 on 2023-11-19 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_num', models.IntegerField(default=0)),
                ('facultyname', models.CharField(max_length=50)),
                ('spvs_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('spvs_interp', models.CharField(max_length=20)),
                ('stud_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('stud_interp', models.CharField(max_length=20)),
                ('peer_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('peer_interp', models.CharField(max_length=20)),
                ('self_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('self_interp', models.CharField(max_length=20)),
                ('load_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('load_interp', models.CharField(default='', max_length=20)),
                ('faculty_stat', models.CharField(default='', max_length=15)),
                ('semester', models.CharField(default='', max_length=15)),
                ('eval_year', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
