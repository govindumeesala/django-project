# Generated by Django 4.2.16 on 2024-10-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Intern_name', models.CharField(max_length=200, null=True)),
                ('Intern_id', models.CharField(max_length=200, null=True)),
                ('Intern_salary', models.FloatField(default=0)),
            ],
        ),
    ]
