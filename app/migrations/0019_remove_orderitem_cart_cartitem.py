# Generated by Django 4.2.5 on 2023-10-12 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_cart_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cart')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
        ),
    ]
