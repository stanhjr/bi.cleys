from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models import (
    AllProjectCalculatorBlock,
    AllProjectPageModel,
    AllProjectSliderModel,
)


class AllProjectSliderModelInline(admin.StackedInline):
    model = AllProjectSliderModel
    extra = 0


class AllProjectCalculatorBlockInline(admin.StackedInline):
    model = AllProjectCalculatorBlock
    extra = 0


@admin.register(AllProjectPageModel)
class AllProjectPageModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [
        AllProjectSliderModelInline,
        AllProjectCalculatorBlockInline
    ]
