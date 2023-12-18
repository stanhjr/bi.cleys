from django.contrib import admin

from apps.website.models.privacy_policy import PrivacyPolicyModel, PrivacyPolicySubBlockModel


class ReviewCommentsModelInline(admin.StackedInline):
    model = PrivacyPolicySubBlockModel
    extra = 0


@admin.register(PrivacyPolicyModel)
class PrivacyPolicyModelAdmin(admin.ModelAdmin):
    inlines = [ReviewCommentsModelInline]
