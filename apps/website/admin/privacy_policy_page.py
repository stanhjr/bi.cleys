from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.privacy_policy import (
    CookieModel,
    CookieSubBlockModel,
    PrivacyPolicyModel,
    PrivacyPolicySubBlockModel,
    TermsAndConditionsModel,
    TermsAndConditionsSubBlockModel,
)


class PrivacyPolicySubBlockInline(admin.StackedInline):
    model = PrivacyPolicySubBlockModel
    extra = 0


@admin.register(PrivacyPolicyModel)
class PrivacyPolicyModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [PrivacyPolicySubBlockInline]


class CookieSubBlockInline(admin.StackedInline):
    model = CookieSubBlockModel
    extra = 0


@admin.register(CookieModel)
class CookieModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [CookieSubBlockInline]


class TermsAndConditionsSubBlockInline(admin.StackedInline):
    model = TermsAndConditionsSubBlockModel
    extra = 0


@admin.register(TermsAndConditionsModel)
class TermsAndConditionsModelAdmin(admin.ModelAdmin):
    inlines = [TermsAndConditionsSubBlockInline]
