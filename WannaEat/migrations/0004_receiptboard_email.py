# Generated by Django 3.0.5 on 2020-07-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WannaEat', '0003_auto_20200726_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptboard',
            name='email',
            field=models.EmailField(default='None', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]