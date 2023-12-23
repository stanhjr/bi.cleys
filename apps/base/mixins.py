from django.core.exceptions import ValidationError
from django.db import models


class SingletonPageMixin(models.Model):
    class Meta:
        abstract = True

    def clean(self):
        if self._meta.model.objects.exclude(
                pk=self.pk,
        ).exists():
            raise ValidationError(f'There can be only one {self._meta.model_name} instance.')

    def delete(self, *args, **kwargs):
        if self._meta.model.objects.count() == 1:
            raise ValidationError(f'There should be at least one {self._meta.model_name} instance.')
        return super().delete(*args, **kwargs)


class NoDeleteModelAdminMixin:
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
