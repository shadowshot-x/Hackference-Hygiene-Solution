# Generated by Django 2.1.4 on 2019-02-08 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('API', models.DecimalField(decimal_places=2, max_digits=10)),
                ('WaterPh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('HDI', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PerCapitaIncome', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]