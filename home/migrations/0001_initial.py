# Generated by Django 3.0.6 on 2022-08-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
