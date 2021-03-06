# Generated by Django 2.1 on 2018-04-26 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20170429_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractive',
            name='expire_date',
            field=models.CharField(auto_created='2018-04-27', max_length=50, verbose_name='Expire date'),
        ),
        migrations.AlterField(
            model_name='useractive',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.User', verbose_name='User ID'),
        ),
    ]
