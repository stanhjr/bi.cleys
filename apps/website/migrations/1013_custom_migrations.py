from django.db import migrations


def copy_data(apps, schema_editor):
    SingleProjectModel = apps.get_model("website", "SingleProjectModel")
    for project in SingleProjectModel.objects.all():
        for idx, block in enumerate(project.specifications_block_two.all()):
            if idx == 0:
                project.specifications_block_one_column_left = block.content
            else:
                project.specifications_block_one_column_right = block.content
        project.save()


def reverse_copy_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0012_singleprojectmodel_specifications_block_one_column_left_and_more"),
    ]

    operations = [
        migrations.RunPython(copy_data, reverse_code=reverse_copy_data),
    ]
