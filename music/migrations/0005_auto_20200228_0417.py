# Generated by Django 3.0.3 on 2020-02-28 04:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_auto_20200228_0415'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seenwork',
            unique_together={('work', 'user')},
        ),
    ]
