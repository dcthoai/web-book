# Generated by Django 4.2.5 on 2023-10-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_order_ispaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageURL',
            field=models.URLField(blank=True, default='static/app/images/icon-camera.png', null=True),
        ),
    ]
