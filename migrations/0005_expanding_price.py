# Generated by Django 4.2.5 on 2024-03-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0004_remove_men_latest_price_expanding'),
    ]

    operations = [
        migrations.AddField(
            model_name='expanding',
            name='price',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]