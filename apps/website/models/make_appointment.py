from django.db import models

from apps.base.mixins import SingletonPageMixin
from apps.base.models import (
    AbstractSliderModel,
    MetaPageAbstractModel,
    TimeStampedModel,
)


class MakeAppointmentPageModel(SingletonPageMixin, MetaPageAbstractModel):
    introduction_title = models.TextField()
    introduction_sub_title = models.TextField()

    def __str__(self):
        return 'Make Appointment Page'


class MakeAppointmentSlider(AbstractSliderModel):
    parent = models.ForeignKey(MakeAppointmentPageModel, on_delete=models.CASCADE, related_name='sliders')


class MakeAppointmentAdvantage(TimeStampedModel):
    title = models.TextField()
    text = models.TextField()
    parent = models.ForeignKey(MakeAppointmentPageModel, on_delete=models.CASCADE, related_name='advantages')


class ServicesAppointment(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feedback(TimeStampedModel):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    post_code = models.CharField(max_length=30)
    estimate_facade_area = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='feedbacks/',
        verbose_name='feedback'
    )
    appointments = models.ManyToManyField("ServicesAppointment", related_name='feedbacks', null=True, blank=True)

    def __str__(self):
        return f'{self.email} {self.created_at}'
