from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose

from apps.base.models import (
    AbstractCalculatorBlock,
    AbstractResultBlock,
    AbstractSliderModel,
    MetaPageAbstractModel,
    TimeStampedModel,
)
from apps.website.models import CategoryPage


class SingleProjectModel(MetaPageAbstractModel):
    related_categories = models.ManyToManyField(CategoryPage, related_name='related_single_projects')
    gallery_title = models.TextField()
    gallery_sub_title = models.TextField()
    show_booking_section = models.BooleanField(default=True)
    specifications_block_one_title = models.TextField()
    specifications_block_one_column_left = models.TextField(null=True, blank=True)
    specifications_block_one_column_right = models.TextField(null=True, blank=True)
    specifications_block_tow_title = models.TextField()

    def __str__(self):
        return f'SingleProjectModel {self.pk}'


class SingleProjectSliderModel(AbstractSliderModel):
    page = models.ForeignKey(SingleProjectModel, on_delete=models.CASCADE, related_name='sliders')


class GalleryItemModel(TimeStampedModel):
    page = models.ForeignKey(SingleProjectModel, on_delete=models.CASCADE, related_name='gallery_items')
    image = models.ImageField(
        upload_to='single_pages/images/',
        verbose_name='image',
        null=True,
        blank=True
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=661,
                height=407,
            )
        ],
        format='JPEG',
    )
    video = models.FileField(
        upload_to='single_pages/videos',
        verbose_name='Video',
        null=True,
        blank=True
    )
    video_poster = models.ImageField(
        upload_to='single_pages/video_posters/',
        verbose_name='video_poster',
        null=True,
        blank=True
    )


class SpecificationsBlockOne(TimeStampedModel):
    page = models.ForeignKey(SingleProjectModel, on_delete=models.CASCADE, related_name='specifications_block_one')
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return f'SpecificationsBlockOne {self.title}'


class SinglePageResultBlock(AbstractResultBlock):
    page = models.OneToOneField(SingleProjectModel, related_name="result_block", on_delete=models.CASCADE)


class SinglePageCalculatorBlock(AbstractCalculatorBlock):
    page = models.OneToOneField(SingleProjectModel, on_delete=models.CASCADE, related_name='calculator_block')


class PreviewItemModel(TimeStampedModel):
    page = models.ForeignKey(SingleProjectModel, on_delete=models.CASCADE, related_name='preview_images')
    image = models.ImageField(
        upload_to='single_pages/preview_images/',
        verbose_name='image',
        null=True,
        blank=True
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=380,
                height=440,
            )
        ],
        format='JPEG',
    )

    def __str__(self):
        return f'Preview Image {self.pk}'
