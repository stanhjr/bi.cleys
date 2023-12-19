import random

from django.db import transaction

from apps.website.models.category_page import CategoryPage
from apps.website.models.single_project import (
    GalleryItemModel,
    PreviewItemModel,
    SinglePageCalculatorBlock,
    SinglePageResultBlock,
    SingleProjectModel,
    SingleProjectSliderModel,
    SpecificationsBlockOne,
    SpecificationsBlockTwo,
)


@transaction.atomic
def generate_fake_projects():
    if SingleProjectModel.objects.count() > 10:
        return
    project = SingleProjectModel.objects.first()
    categories = list(CategoryPage.objects.exclude(name='Isolatie').all())
    for category in CategoryPage.objects.exclude(name='Isolatie').all():
        for i in range(3):
            new_project = SingleProjectModel.objects.create(
                **{field.name: getattr(project, field.name) for field in SingleProjectModel._meta.fields if
                   field.name not in ('id', 'page', 'created_at', 'updated_at', 'related_categories')}
            )
            for random_categories in random.sample(categories, 2):
                new_project.related_categories.add(random_categories)

            for slider in project.sliders.all():
                SingleProjectSliderModel.objects.create(
                    page=new_project,
                    **{field.name: getattr(slider, field.name) for field in SingleProjectSliderModel._meta.fields if
                       field.name not in ('id', 'page', 'created_at', 'updated_at')}
                )

            for gallery in project.gallery_items.all():
                GalleryItemModel.objects.create(
                    page=new_project,
                    **{field.name: getattr(gallery, field.name) for field in GalleryItemModel._meta.fields if
                       field.name not in ('id', 'page', 'created_at', 'updated_at')}
                )

            for spec in project.specifications_block_one.all():
                SpecificationsBlockOne.objects.create(
                    page=new_project,
                    **{field.name: getattr(spec, field.name) for field in SpecificationsBlockOne._meta.fields if
                       field.name not in ('id', 'page', 'created_at', 'updated_at')}
                )

            for spec in project.specifications_block_two.all():
                SpecificationsBlockTwo.objects.create(
                    page=new_project,
                    **{field.name: getattr(spec, field.name) for field in SpecificationsBlockTwo._meta.fields if
                       field.name not in ('id', 'page', 'created_at', 'updated_at')}
                )

            res_block = SinglePageResultBlock.objects.last()
            SinglePageResultBlock.objects.create(
                page=new_project,
                **{field.name: getattr(res_block, field.name) for field in SinglePageResultBlock._meta.fields if
                   field.name not in ('id', 'page', 'created_at', 'updated_at')}
            )

            for img in project.preview_images.all():
                PreviewItemModel.objects.create(
                    page=new_project,
                    **{field.name: getattr(img, field.name) for field in PreviewItemModel._meta.fields if
                       field.name not in ('id', 'page', 'created_at', 'updated_at')}
                )
