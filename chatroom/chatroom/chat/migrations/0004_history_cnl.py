# Generated by Django 2.1.7 on 2019-03-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20190317_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='cnl',
            field=models.CharField(default=0, max_length=30, null=True),
        ),
    ]
