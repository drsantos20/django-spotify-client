# Generated by Django 2.2 on 2019-05-24 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='shazam@dc.com', max_length=15),
            preserve_default=False,
        ),
    ]
