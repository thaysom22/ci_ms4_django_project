# Generated by Django 3.2.4 on 2021-07-06 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscribe', '0002_subscription_stripe_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='email',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
