# Generated by Django 4.1.4 on 2023-02-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reentry_todo', '0015_alter_comment_created_at_likebutton'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='LikeButton',
        ),
    ]