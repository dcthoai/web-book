# Generated by Django 4.2.5 on 2023-10-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_product_category_alter_sliderhome_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
