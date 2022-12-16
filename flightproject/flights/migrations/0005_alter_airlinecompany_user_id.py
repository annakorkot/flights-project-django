# Generated by Django 4.1 on 2022-11-12 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0004_alter_airlinecompany_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airlinecompany',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline_companies', to=settings.AUTH_USER_MODEL),
        ),
    ]