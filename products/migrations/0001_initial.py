# Generated by Django 3.2.2 on 2021-05-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('P_ID', models.AutoField(primary_key=True, serialize=False)),
                ('P_NAME', models.CharField(max_length=100)),
                ('P_IMG', models.ImageField(upload_to='products/images')),
                ('P_DESC', models.CharField(max_length=1000)),
                ('P_PRICE', models.FloatField()),
                ('P_STOCK', models.IntegerField()),
                ('P_STATUS', models.IntegerField(choices=[(0, 'INACTIVE'), (1, 'ACTIVE')])),
            ],
        ),
    ]
