# Generated by Django 3.2.13 on 2023-09-16 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_story', '0013_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='storyId',
        ),
        migrations.AlterField(
            model_name='comment',
            name='chapterId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_story.chapter'),
            preserve_default=False,
        ),
    ]