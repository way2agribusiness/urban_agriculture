# Generated by Django 4.2 on 2024-05-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0030_review_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]
