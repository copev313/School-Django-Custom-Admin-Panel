# Generated by Django 4.0.2 on 2022-02-26 01:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(default='ABC1234-00', max_length=15),
        ),
        migrations.AddField(
            model_name='course',
            name='grade_type',
            field=models.CharField(choices=[('G', 'Graded'), ('U', 'Ungraded'), ('P', 'Pass/Fail'), ('E', 'Exam')], default='G', max_length=15),
        ),
        migrations.AddField(
            model_name='course',
            name='year_taught',
            field=models.IntegerField(default=1997, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2999)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default='1970-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='years_studied',
            field=models.SmallIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(19)]),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'year_taught')},
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=70)),
                ('building', models.CharField(max_length=50)),
                ('office_number', models.CharField(max_length=30)),
                ('degree_type', models.CharField(max_length=60)),
                ('years_tenured', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('courses', models.ManyToManyField(blank=True, related_name='instructors', to='core.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='year',
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instructor'),
        ),
    ]
