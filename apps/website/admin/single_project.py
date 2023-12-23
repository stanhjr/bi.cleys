from django.contrib import admin

from apps.website.models.single_project import (
    GalleryItemModel,
    PreviewItemModel,
    SinglePageCalculatorBlock,
    SinglePageResultBlock,
    SingleProjectModel,
    SingleProjectSliderModel,
    SpecificationsBlockOne,
)


class SingleProjectSliderModelInline(admin.StackedInline):
    model = SingleProjectSliderModel
    extra = 0


class GalleryItemModelInline(admin.StackedInline):
    model = GalleryItemModel
    extra = 0


class SpecificationsBlockOneInline(admin.StackedInline):
    model = SpecificationsBlockOne
    extra = 0


class SinglePageResultBlockInline(admin.StackedInline):
    model = SinglePageResultBlock
    extra = 0


class SinglePageCalculatorBlockInline(admin.StackedInline):
    model = SinglePageCalculatorBlock
    extra = 0


class PreviewItemModelInline(admin.StackedInline):
    model = PreviewItemModel
    extra = 0


@admin.register(SingleProjectModel)
class SingleProjectModelAdmin(admin.ModelAdmin):
    inlines = [
        SingleProjectSliderModelInline,
        GalleryItemModelInline,
        SpecificationsBlockOneInline,
        SinglePageResultBlockInline,
        SinglePageCalculatorBlockInline,
        PreviewItemModelInline,
    ]
