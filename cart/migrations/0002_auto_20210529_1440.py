# Generated by Django 3.2.2 on 2021-05-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='P_ID',
            new_name='PRODUCT',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='C_QTY',
            new_name='QTY',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='U_ID',
            new_name='USER',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='C_DATE',
        ),
        migrations.AddField(
            model_name='cart',
            name='DATE',
            field=models.DateTimeField(auto_now=True),
        ),
    ]