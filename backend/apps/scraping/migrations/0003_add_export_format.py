# Generated by Django 5.0.1 on 2025-07-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_alter_xaccount_options_alter_xaccount_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapingjob',
            name='export_format',
            field=models.CharField(choices=[('json', 'JSON'), ('csv', 'CSV')], default='json', help_text='Formato de exportación', max_length=10),
        ),
        migrations.AlterField(
            model_name='scrapingjob',
            name='name',
            field=models.CharField(blank=True, default='', help_text='Nombre descriptivo opcional', max_length=200),
        ),
    ]
