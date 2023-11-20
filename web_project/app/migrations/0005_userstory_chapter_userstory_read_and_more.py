# Generated by Django 4.2.7 on 2023-11-18 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_userstory_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.chapters'),
        ),
        migrations.AddField(
            model_name='userstory',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
