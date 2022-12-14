# Generated by Django 4.1.3 on 2022-11-14 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='products.product')),
            ],
        ),
        migrations.AddIndex(
            model_name='trackproduct',
            index=models.Index(fields=['created_at'], name='products_tr_created_3e611e_idx'),
        ),
    ]
