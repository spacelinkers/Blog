# Generated by Django 2.1.4 on 2019-04-04 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190404_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=150, null=True, verbose_name='Sub Title'),
        ),
    ]