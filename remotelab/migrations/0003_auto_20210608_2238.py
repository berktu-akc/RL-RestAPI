# Generated by Django 3.2.4 on 2021-06-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotelab', '0002_auto_20210608_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotelab',
            name='Channel1',
            field=models.CharField(default='', max_length=1, verbose_name='Channel1'),
        ),
        migrations.AlterField(
            model_name='remotelab',
            name='Channel2',
            field=models.CharField(default='', max_length=2, verbose_name='Channel2'),
        ),
    ]