# Generated by Django 2.1.4 on 2019-02-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0003_auto_20190209_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='Photo',
            field=models.CharField(default='yo', max_length=500),
            preserve_default=False,
        ),
    ]
