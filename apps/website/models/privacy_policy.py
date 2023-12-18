from ckeditor.fields import RichTextField
from django.db import models

from apps.base.mixins import SingletonPageMixin
from apps.base.models import MetaPageAbstractModel, TimeStampedModel


class PrivacyPolicyModel(SingletonPageMixin, MetaPageAbstractModel):
    head_title = models.TextField(default='Privacy policy')
    title = models.TextField()
    content = RichTextField()

    def __str__(self):
        return 'Privacy Policy'


class PrivacyPolicySubBlockModel(TimeStampedModel):
    page = models.ForeignKey(PrivacyPolicyModel, on_delete=models.CASCADE, related_name='sub_blocks')
    title = models.TextField()
    content = RichTextField()

    def __str__(self):
        return f'Privacy Policy sub block {self.pk}'
