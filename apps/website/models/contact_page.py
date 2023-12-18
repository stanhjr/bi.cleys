from django.db import models

from apps.base.mixins import SingletonPageMixin
from apps.base.models import (
    AbstractSliderModel,
    MetaPageAbstractModel,
    TimeStampedModel,
)


class ContactPageModel(SingletonPageMixin, MetaPageAbstractModel):
    address_title = models.CharField(max_length=255)
    address_link = models.URLField(max_length=250)
    link_title = models.CharField(max_length=255, default='Algemene voorwaarden')

    def __str__(self):
        return 'Contact Page'


class ContactImageSliderModel(AbstractSliderModel):
    page = models.ForeignKey(ContactPageModel, on_delete=models.CASCADE, related_name='sliders')


class AddressParagraphModel(TimeStampedModel):
    paragraph = models.CharField(max_length=255, null=True, blank=True)
    page = models.ForeignKey(ContactPageModel, on_delete=models.CASCADE, related_name='address_paragraphs')

    def __str__(self):
        return self.paragraph


class ContactFeedbackModel(TimeStampedModel):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    post_code = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return f"{self.full_name} {self.created_at}"
