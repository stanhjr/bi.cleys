from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose

from apps.base.mixins import SingletonPageMixin
from apps.base.models import AbstractMetaModel, TimeStampedModel


class MetadataModel(SingletonPageMixin, AbstractMetaModel):

    def __str__(self):
        return 'Meta data'


class ContactModel(SingletonPageMixin, TimeStampedModel):
    phone = models.CharField(
        max_length=25,
        verbose_name='phone'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return 'Contact Block Model'


class FooterModel(SingletonPageMixin, TimeStampedModel):
    description = models.TextField()

    def __str__(self):
        return 'Footer Block Model'


class AppointmentModel(SingletonPageMixin, TimeStampedModel):
    image = models.ImageField(
        upload_to='appointment/',
        verbose_name='appointment_image'
    )
    sub_title = models.TextField(default='Afspraak maken')
    description = models.TextField(default='We komen langs met vrijblijvend advies.')

    def __str__(self):
        return 'Appointment Block Model'


class CalculatedBlockModel(SingletonPageMixin, TimeStampedModel):
    title = models.TextField()
    sub_title = models.TextField()
    sub_title_two = models.TextField()
    description = models.TextField()
    description_two = models.TextField()
    new_construction_text = models.TextField()
    renovation_text = models.TextField()
    image = models.ImageField(
        upload_to='calculate_block/',
        verbose_name='image'
    )
    image_cut = ImageSpecField(
        source='image',
        processors=[
            Transpose(),
            ResizeToFill(
                width=493,
                height=628,
            )
        ],
        format='JPEG',
    )

    def __str__(self):
        return "Calculate Block Model"


class ReviewsStarsModel(SingletonPageMixin, TimeStampedModel):
    all_reviews = models.IntegerField()
    title = models.TextField(blank=True)
    stars = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return 'Reviews'


class ReviewCommentsModel(TimeStampedModel):
    comment = models.TextField()
    review = models.ForeignKey('ReviewsStarsModel', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Review: {self.pk}'
