from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.website'

    def ready(self):
        from apps.website.signals import send_email_after_contact_feedback_signal # noqa
        from apps.website.signals import send_email_after_feedback_signal # noqa

