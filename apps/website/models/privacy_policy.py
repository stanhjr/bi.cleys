from ckeditor.fields import RichTextField
from django.db import models

from apps.base.mixins import SingletonPageMixin
from apps.base.models import MetaPageAbstractModel, TimeStampedModel


class BasePolicyAbstractModel(MetaPageAbstractModel, TimeStampedModel):
    head_title = models.TextField(default="Privacy policy")
    title = models.TextField()
    content = RichTextField()

    class Meta:
        abstract = True


class BasePolicySubBlockAbstractModel(TimeStampedModel):
    title = models.TextField()
    content = RichTextField()

    class Meta:
        abstract = True


class PrivacyPolicyModel(BasePolicyAbstractModel):

    def __str__(self):
        return "Privacy Policy"


class PrivacyPolicySubBlockModel(BasePolicySubBlockAbstractModel):
    page = models.ForeignKey(PrivacyPolicyModel, on_delete=models.CASCADE, related_name="sub_blocks")

    def __str__(self):
        return f"Privacy Policy sub block {self.pk}"


class CookieModel(BasePolicyAbstractModel):
    def __str__(self):
        return "Cookie Policy"


class CookieSubBlockModel(BasePolicySubBlockAbstractModel):
    page = models.ForeignKey(CookieModel, on_delete=models.CASCADE, related_name="sub_blocks")

    def __str__(self):
        return f"Cookie sub block {self.pk}"


class TermsAndConditionsModel(BasePolicyAbstractModel):

    def __str__(self):
        return "Terms And Conditions"


class TermsAndConditionsSubBlockModel(BasePolicySubBlockAbstractModel):
    page = models.ForeignKey(TermsAndConditionsModel, on_delete=models.CASCADE, related_name="sub_blocks")

    def __str__(self):
        return f"Terms And Conditions {self.pk}"
