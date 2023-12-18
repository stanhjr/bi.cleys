from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.about_us import (
    AboutUsHistoryModel,
    AboutUsImageSliderModel,
    AboutUsPageModel,
    AboutUsTeamMemberModel,
)


class AboutUsHistoryInline(admin.StackedInline):
    model = AboutUsHistoryModel
    extra = 0


class AboutUsTeamMemberInline(admin.StackedInline):
    model = AboutUsTeamMemberModel
    extra = 0


class AboutUsImageSliderInline(admin.StackedInline):
    model = AboutUsImageSliderModel
    extra = 0


@admin.register(AboutUsPageModel)
class AboutUsPageAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [
        AboutUsImageSliderInline,
        AboutUsTeamMemberInline,
        AboutUsHistoryInline
    ]
