# Generated by Django 3.1.3 on 2021-05-18 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201220_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendShipStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ab', 'ab'), ('ba', 'ba'), ('axb', 'axb')], max_length=3)),
                ('user_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.userinfo')),
                ('user_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='user.userinfo')),
            ],
        ),
    ]
