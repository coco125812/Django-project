# Generated by Django 5.0 on 2023-12-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='laksh', max_length=100),
            preserve_default=False,
        ),
    ]