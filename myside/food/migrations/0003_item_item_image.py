# Generated by Django 4.2.4 on 2023-12-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg', max_length=500),
        ),
    ]