# Generated by Django 3.0.6 on 2020-09-07 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='visitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Visitor'),
        ),
    ]