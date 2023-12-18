from ckeditor.fields import RichTextField
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose

from apps.base.mixins import SingletonPageMixin
from apps.base.models import (
    AbstractSliderModel,
    MetaPageAbstractModel,
    TimeStampedModel,
)


class AboutUsPageModel(SingletonPageMixin, MetaPageAbstractModel):
    introduction_title = models.TextField()
    introduction_content = RichTextField()
    introduction_small_image = models.ImageField(
        upload_to='about_us/introduction_small_images/',
        verbose_name='introduction_small_image'
    )
    introduction_small_image_cut = ImageSpecField(
        source='introduction_small_image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=265,
                height=269,
            )
        ],
        format='JPEG',
    )
    introduction_big_image = models.ImageField(
        upload_to='about_us/introduction_big_images/',
        verbose_name='introduction_big_image'
    )
    introduction_big_image_cut = ImageSpecField(
        source='introduction_big_image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=386,
                height=394,
            )
        ],
        format='JPEG',
    )
    team_title = models.CharField(max_length=255)

    def __str__(self):
        return 'About Us Page'


class AboutUsImageSliderModel(AbstractSliderModel):
    about_us = models.ForeignKey(AboutUsPageModel, on_delete=models.CASCADE, related_name='sliders')


class AboutUsTeamMemberModel(TimeStampedModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='about_us/team_members/',
        verbose_name='about_us_team_member'
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=386,
                height=394,
            )
        ],
        format='JPEG',
    )
    about_us = models.ForeignKey(AboutUsPageModel, on_delete=models.CASCADE, related_name='team_members')


class AboutUsHistoryModel(TimeStampedModel):
    year = models.CharField(max_length=10)
    title = models.TextField()
    image = models.ImageField(
        upload_to='about_us/histories/',
        verbose_name='about_us_history'
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=386,
                height=394,
            )
        ],
        format='JPEG',
    )
    about_us = models.ForeignKey(AboutUsPageModel, on_delete=models.CASCADE, related_name='histories')
