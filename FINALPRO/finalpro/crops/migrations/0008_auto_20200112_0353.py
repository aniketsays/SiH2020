# Generated by Django 3.0.2 on 2020-01-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0007_remove_inputcrops_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
    ]