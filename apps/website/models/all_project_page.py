from django.db import models

from apps.base.mixins import SingletonPageMixin
from apps.base.models import (
    AbstractCalculatorBlock,
    AbstractSliderModel,
    MetaPageAbstractModel,
)


class AllProjectPageModel(SingletonPageMixin, MetaPageAbstractModel):
    title = models.TextField()
    sub_title = models.TextField()
    show_booking_section = models.BooleanField(default=True)

    def __str__(self):
        return 'AllProjectPageModel'


class AllProjectSliderModel(AbstractSliderModel):
    page = models.ForeignKey(AllProjectPageModel, on_delete=models.CASCADE, related_name='sliders')


class AllProjectCalculatorBlock(AbstractCalculatorBlock):
    page = models.OneToOneField(AllProjectPageModel, on_delete=models.CASCADE, related_name='calculator_block')
