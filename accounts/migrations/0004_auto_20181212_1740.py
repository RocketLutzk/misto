# Generated by Django 2.1.3 on 2018-12-12 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181212_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='boxs2', to=settings.AUTH_USER_MODEL),
        ),
    ]
