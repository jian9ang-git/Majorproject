# Generated by Django 3.1.2 on 2021-05-04 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sweet', '0002_auto_20210429_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='products',
        ),
        migrations.AlterField(
            model_name='adress',
            name='post_index',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='adresses',
            field=models.ManyToManyField(related_name='customer_adresses', to='sweet.Adress'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='sweet.category'),
        ),
    ]
