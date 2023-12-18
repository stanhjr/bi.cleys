from ckeditor.fields import RichTextField
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose

from apps.base.models import (
    AbstractCalculatorBlock,
    AbstractResultBlock,
    AbstractSliderModel,
    IntroductionAbstractModel,
    MetaPageAbstractModel,
    SlugNameMixin,
    TimeStampedModel,
)


class CategoryPage(SlugNameMixin, IntroductionAbstractModel, MetaPageAbstractModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    related_projects_block_title = models.TextField(null=True, blank=True)
    related_projects_block_sub_title = models.TextField(null=True, blank=True)
    completed_projects_block_title = models.TextField(null=True, blank=True)
    completed_projects_block_sub_title = models.TextField(null=True, blank=True)
    completed_projects_block_description = models.TextField(null=True, blank=True)
    show_booking_section = models.BooleanField(default=False)
    index_preview_icon = models.FileField(
        upload_to='index_preview_icons/',
        verbose_name='index_preview_icon',
        blank=True,
        null=True
    )
    index_preview_text = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['order_by']

    def __str__(self):
        return self.name


class CategorySliderModel(AbstractSliderModel):
    page = models.ForeignKey(CategoryPage, on_delete=models.CASCADE, related_name='sliders')


class RelatedProjects(TimeStampedModel):
    page = models.ForeignKey(CategoryPage, on_delete=models.CASCADE, related_name='related_projects')
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='related_projects/',
        verbose_name='image'
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=330,
                height=363,
            )
        ],
        format='JPEG',
    )
    path_to_page = models.CharField(null=True, blank=True, max_length=100)
    button_text = models.CharField(default='Meer informatie', max_length=60)


class CalculatorBlock(AbstractCalculatorBlock):
    page = models.OneToOneField(CategoryPage, on_delete=models.CASCADE, related_name='calculator_block')


class ContentBlock(TimeStampedModel):
    page = models.OneToOneField(CategoryPage, related_name="content_block", on_delete=models.CASCADE)
    title = models.TextField()
    sub_title = models.TextField()
    content = RichTextField(verbose_name='Content Block Content')
    image = models.ImageField(
        upload_to='content_block/before/',
        verbose_name='image'
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=463,
                height=500,
            )
        ],
        format='JPEG',
    )


class VideoBlock(TimeStampedModel):
    page = models.OneToOneField(CategoryPage, related_name="video_block", on_delete=models.CASCADE)
    title = models.TextField()
    sub_title = models.TextField()
    video = models.FileField(
        upload_to='video_block/',
        verbose_name='Video'
    )
    video_poster = models.ImageField(
        upload_to='video_poster/',
        verbose_name='video_poster'
    )


class ProjectBlock(TimeStampedModel):
    page = models.OneToOneField(CategoryPage, related_name="project_block", on_delete=models.CASCADE)
    title = models.TextField()
    sub_title = models.TextField()
    content = models.TextField()


class ResultBlock(AbstractResultBlock):
    page = models.OneToOneField(CategoryPage, related_name="result_block", on_delete=models.CASCADE)


class AnimationBlock(TimeStampedModel):
    class AnimationType(models.TextChoices):
        CREPI = 'crepi', 'crepi'
        DAKWERGEN = 'dakwerken', 'dakwerken'
        RAMEN = 'ramen_deuren', 'ramen_deuren'
        GEBELISOLATIE = 'gevelisolatie', 'gevelisolatie'

    animation_type = models.CharField(
        max_length=30,
        choices=AnimationType.choices,
        default=AnimationType.CREPI
    )
    animation_turn = models.BooleanField(default=True)
    page = models.OneToOneField(CategoryPage, related_name="animation_block", on_delete=models.CASCADE)


class CTAOptionalBlock(TimeStampedModel):
    page = models.OneToOneField(CategoryPage, related_name="cta", on_delete=models.CASCADE)
    title = models.TextField()
    sub_title = models.TextField()
