# Generated by Django 4.1.4 on 2023-02-14 15:56

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reentry_todo', '0012_alter_comment_created_at_delete_resourcepages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 14, 15, 56, 11, 294168, tzinfo=datetime.timezone.utc)),
        ),
    ]
