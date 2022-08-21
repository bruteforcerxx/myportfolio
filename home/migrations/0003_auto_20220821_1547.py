# Generated by Django 3.0.6 on 2022-08-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220821_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitordata',
            name='latlng',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='visitordata',
            name='sn',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
