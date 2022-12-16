# Generated by Django 4.1 on 2022-11-10 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_user_roles_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='administrators', to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.user_role'),
        ),
    ]