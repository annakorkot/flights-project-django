# Generated by Django 4.1 on 2022-11-10 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_administrator_user_id_alter_user_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='accounts.user'),
        ),
    ]