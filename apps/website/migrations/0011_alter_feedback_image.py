# Generated by Django 5.0 on 2023-12-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_categorypage_options_delete_descriptionblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='feedbacks/', verbose_name='feedback'),
        ),
    ]