# Generated by Django 3.0.6 on 2020-09-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200907_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='visitor',
            field=models.CharField(default='Anonymous', max_length=200),
            preserve_default=False,
        ),
    ]
