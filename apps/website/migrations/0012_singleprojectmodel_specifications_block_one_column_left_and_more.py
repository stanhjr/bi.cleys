# Generated by Django 5.0 on 2023-12-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_feedback_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleprojectmodel',
            name='specifications_block_one_column_left',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='singleprojectmodel',
            name='specifications_block_one_column_right',
            field=models.TextField(blank=True, null=True),
        ),
    ]
