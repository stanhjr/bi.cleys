from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models import JobsPageModel
from apps.website.models.jobs_page import JobsImageSliderModel, VacationModel


class VacationModelInline(admin.StackedInline):
    model = VacationModel
    extra = 0


class JobsImageSliderModelSliderInline(admin.StackedInline):
    model = JobsImageSliderModel
    extra = 0


@admin.register(JobsPageModel)
class AboutUsPageAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [
        JobsImageSliderModelSliderInline,
        VacationModelInline
    ]
