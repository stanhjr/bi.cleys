from django.contrib import admin
from django.db import models

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.make_appointment import (
    Feedback,
    MakeAppointmentAdvantage,
    MakeAppointmentPageModel,
    MakeAppointmentSlider,
    ServicesAppointment,
)
from apps.website.widgets import CheckboxSelectMultiple


class MakeAppointmentSliderInline(admin.StackedInline):
    model = MakeAppointmentSlider
    extra = 0


class MakeAppointmentAdvantageInline(admin.StackedInline):
    model = MakeAppointmentAdvantage
    extra = 0


@admin.register(MakeAppointmentPageModel)
class MakeAppointmentPageModelAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [MakeAppointmentSliderInline, MakeAppointmentAdvantageInline]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'created_at')
    search_fields = ('email', 'full_name')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')


@admin.register(ServicesAppointment)
class ServicesAppointmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
