# Generated by Django 5.0.3 on 2024-03-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]