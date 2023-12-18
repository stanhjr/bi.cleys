from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.premium_loans_page import PremiumLoansPageModel, PremiumLoansSliderModel


class PremiumLoansSliderInline(admin.StackedInline):
    model = PremiumLoansSliderModel
    extra = 0


@admin.register(PremiumLoansPageModel)
class PremiumLoansPageModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [PremiumLoansSliderInline, ]
