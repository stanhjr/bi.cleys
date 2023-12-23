from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill, Transpose


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractMetaModel(TimeStampedModel):
    meta_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='meta tittle'
    )
    meta_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='meta description'
    )

    class Meta:
        abstract = True


class MetaPageAbstractModel(TimeStampedModel):
    meta_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='meta tittle'
    )
    meta_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='meta description'
    )

    show_slider = models.BooleanField(default=False)
    """True if the banner should have a slider"""

    show_send_reviews_button = models.BooleanField(default=True)
    """True if the banner has a redirect button"""

    class Meta:
        abstract = True


class AbstractSliderModel(TimeStampedModel):
    """
    Abstract base model for sliders with common fields like title, body, and banner image.

    Attributes:
        slider_title (str): The title of the slider.
        slider_body (str): The body or description associated with the slider.
        banner_image (ImageField): The image file for the slider banner.
            resized to fit the dimensions 1425x370 pixels.

    Note:
        To associate a slider with a specific page, create a ForeignKey in your concrete
        model that inherits from this abstract base class. For example:

        ```python
        class YourSliderModel(AbstractSliderModel):
            page = models.ForeignKey(
                'YourPageModel',
                on_delete=models.CASCADE,
                related_name='sliders',
            )
        ```
    """
    slider_title = models.TextField()
    slider_body = models.TextField()
    banner_image = models.ImageField(
        upload_to='sliders/banner_fills/',
        verbose_name='banner_fill',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class SlugNameMixin(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class IntroductionAbstractModel(models.Model):
    introduction_left_title = models.TextField()
    introduction_left_sub_title = models.TextField()
    introduction_left_intro = models.TextField(blank=True, null=True)
    introduction_left_content = RichTextField(verbose_name='Introduction Left Content')
    introduction_right_sub_title = models.TextField()
    introduction_right_header_title = models.TextField()
    introduction_right_content = RichTextField(verbose_name='Introduction Right Content')
    order_by = models.IntegerField(default=0)

    class Meta:
        abstract = True

    @property
    def get_introduction_right_content(self):
        content = self.introduction_right_content.replace('<ul>', '')
        content = content.replace('</ul>', '')
        return content


class AbstractResultBlock(TimeStampedModel):
    title = models.TextField()
    sub_title = models.TextField()
    image_before = models.ImageField(
        upload_to='result_block/before/',
        verbose_name='image_before'
    )
    image_before_cut = ImageSpecField(
        source='image_before',
        processors=[
            Transpose(),
            ResizeToFill(
                width=943,
                height=557,
            )
        ],
        format='JPEG',
    )
    image_after = models.ImageField(
        upload_to='result_block/after/',
        verbose_name='image_after'
    )
    image_after_cut = ImageSpecField(
        source='image_after',
        processors=[
            Transpose(),
            ResizeToFill(
                width=943,
                height=557,
            )
        ],
        format='JPEG',
    )

    class Meta:
        abstract = True


class AbstractCalculatorBlock(TimeStampedModel):
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

    class Meta:
        abstract = True

    def __str__(self):
        return "Calculator Image"
