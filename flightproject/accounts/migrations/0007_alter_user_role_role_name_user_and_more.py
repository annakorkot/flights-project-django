# Generated by Django 4.1 on 2022-11-12 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_administrator_user_id_alter_customer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_role',
            name='role_name',
            field=models.CharField(blank=True, choices=[('Customer', 'Customer'), ('Company', 'Airlinecompany'), ('Admin', 'Administrator')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.user_role')),
            ],
        ),
        migrations.AlterField(
            model_name='administrator',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='administrators', to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='accounts.user'),
        ),
    ]
