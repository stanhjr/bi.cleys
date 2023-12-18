from django.contrib import admin

from apps.base.mixins import NoDeleteModelAdminMixin
from apps.website.models.contact_page import (
    AddressParagraphModel,
    ContactFeedbackModel,
    ContactImageSliderModel,
    ContactPageModel,
)


class ContactImageSliderInline(admin.StackedInline):
    model = ContactImageSliderModel
    extra = 0


class AddressParagraphInline(admin.StackedInline):
    model = AddressParagraphModel
    extra = 0


@admin.register(ContactPageModel)
class ContactPageAdmin(NoDeleteModelAdminMixin, admin.ModelAdmin):
    inlines = [
        ContactImageSliderInline,
        AddressParagraphInline,
    ]


@admin.register(ContactFeedbackModel)
class ContactFeedbackAdmin(admin.ModelAdmin):
    search_fields = ('email', 'full_name')
    list_display = ('email', 'full_name', 'created_at')

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')
