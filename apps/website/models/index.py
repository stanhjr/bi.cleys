from django.db import models

from apps.base.mixins import SingletonPageMixin
from apps.base.models import (
    AbstractCalculatorBlock,
    AbstractSliderModel,
    IntroductionAbstractModel,
    MetaPageAbstractModel,
)


class IndexPageModel(SingletonPageMixin, IntroductionAbstractModel, MetaPageAbstractModel):
    show_booking_section = models.BooleanField(default=True)
    overview_title = models.TextField()
    overview_sub_title = models.TextField()
    completed_projects_block_title = models.TextField()
    completed_projects_block_sub_title = models.TextField()
    completed_projects_block_description = models.TextField()

    def __str__(self):
        return 'IndexPageModel'


class IndexSliderModel(AbstractSliderModel):
    page = models.ForeignKey(IndexPageModel, on_delete=models.CASCADE, related_name='sliders')


class IndexCalculatorBlock(AbstractCalculatorBlock):
    page = models.OneToOneField(IndexPageModel, on_delete=models.CASCADE, related_name='calculator_block')
