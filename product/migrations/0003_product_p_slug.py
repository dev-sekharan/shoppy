# Generated by Django 3.2.2 on 2021-05-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_p_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='P_SLUG',
            field=models.SlugField(max_length=40, null=True),
        ),
    ]