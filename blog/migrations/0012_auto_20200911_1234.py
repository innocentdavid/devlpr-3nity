# Generated by Django 3.0.6 on 2020-09-11 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderator',
            name='visitor',
        ),
        migrations.AddField(
            model_name='moderator',
            name='user',
            field=models.CharField(default='AnonymousUser', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Moderator'),
        ),
    ]
