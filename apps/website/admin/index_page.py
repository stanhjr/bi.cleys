from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.index import (
    IndexCalculatorBlock,
    IndexPageModel,
    IndexSliderModel,
)


class IndexSliderModelInline(admin.StackedInline):
    model = IndexSliderModel
    extra = 0


class IndexCalculatorBlockInline(admin.StackedInline):
    model = IndexCalculatorBlock
    extra = 0


@admin.register(IndexPageModel)
class IndexPageModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [
        IndexSliderModelInline,
        IndexCalculatorBlockInline,
    ]
