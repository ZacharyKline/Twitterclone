# Generated by Django 2.2.7 on 2019-11-20 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0003_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='tweet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='twitterclone.Tweet'),
            preserve_default=False,
        ),
    ]