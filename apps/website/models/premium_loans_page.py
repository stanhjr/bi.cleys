from ckeditor.fields import RichTextField
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose

from apps.base.mixins import SingletonPageMixin
from apps.base.models import AbstractSliderModel, MetaPageAbstractModel


class PremiumLoansPageModel(SingletonPageMixin, MetaPageAbstractModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.URLField(max_length=255)
    renovation_title = models.TextField(null=True)
    renovation_sub_title = models.TextField(null=True)
    renovation_block = RichTextField(verbose_name='Renovation Block')
    renovation_premium_title = models.TextField(null=True)
    renovation_premium_sub_title = models.TextField(null=True)
    renovation_premium_image = models.ImageField(
        upload_to='premium_loans_page/',
        verbose_name='personal situation image',
        null=True
    )
    renovation_premium_block = RichTextField(verbose_name='Renovation Premium Block')
    get_premium_block_left_title = models.TextField(null=True)
    get_premium_block_left_sub_title = models.TextField(null=True)
    get_premium_block_left = RichTextField(verbose_name='Get Premium Block Left')
    get_premium_block_right_title = models.TextField(null=True)
    get_premium_block_right = RichTextField(verbose_name='Get Premium Block Right')
    personal_situation_title = models.TextField(null=True)
    personal_situation_sub_title = models.TextField(null=True)
    personal_situation_block = RichTextField(verbose_name='Personal Situation Block')
    personal_situation_image = models.ImageField(
        upload_to='premium_loans_page/',
        verbose_name='personal situation image'
    )
    personal_situation_image_cut = ImageSpecField(
        source='personal_situation_image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=1425,
                height=370,
            )
        ],
        format='JPEG',
    )

    def __str__(self):
        return 'Premium Loans Page Model'


class PremiumLoansSliderModel(AbstractSliderModel):
    page = models.ForeignKey(PremiumLoansPageModel, on_delete=models.CASCADE, related_name='sliders')
