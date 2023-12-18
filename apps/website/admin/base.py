from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.base import (
    AppointmentModel,
    CalculatedBlockModel,
    ContactModel,
    FooterModel,
    MetadataModel,
    ReviewCommentsModel,
    ReviewsStarsModel,
)


@admin.register(MetadataModel)
class MetadataModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(AppointmentModel)
class AppointmentModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ContactModel)
class ContactModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(FooterModel)
class FooterModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    pass


class ReviewCommentsModelInline(admin.StackedInline):
    model = ReviewCommentsModel
    extra = 0


@admin.register(ReviewsStarsModel)
class ReviewsStarsModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [ReviewCommentsModelInline]


@admin.register(CalculatedBlockModel)
class CalculatedBlockModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    pass
