from ckeditor.fields import RichTextField
from django.db import models

from apps.base.models import (
    AbstractSliderModel,
    IntroductionAbstractModel,
    MetaPageAbstractModel,
    SlugNameMixin,
    TimeStampedModel,
)


class JobsPageModel(IntroductionAbstractModel, MetaPageAbstractModel):
    jobs_header = models.TextField()
    introduction_left_content = RichTextField(verbose_name='Introduction Left Content', null=True, blank=True)

    def __str__(self):
        return 'Jobs Page'


class JobsImageSliderModel(AbstractSliderModel):
    page = models.ForeignKey(JobsPageModel, on_delete=models.CASCADE, related_name='sliders')


class VacationModel(SlugNameMixin, TimeStampedModel):
    page = models.ForeignKey(JobsPageModel, on_delete=models.CASCADE, related_name='vacations')
    title = models.TextField()
    description = models.TextField()
    content = RichTextField()
    order_by = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order_by', )
