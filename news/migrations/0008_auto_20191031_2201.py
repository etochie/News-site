# Generated by Django 2.2.6 on 2019-10-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_articlestatistic'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.DeleteModel(
            name='ArticleStatistic',
        ),
    ]