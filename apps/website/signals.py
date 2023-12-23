from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.website.models.contact_page import ContactFeedbackModel
from apps.website.models.make_appointment import Feedback


@receiver(post_save, sender=ContactFeedbackModel)
def send_email_after_contact_feedback_signal(sender, instance: ContactFeedbackModel | Feedback, created, **kwargs):
    """
    Send Email after contact feedback create
    """
    if created:
        EmailMessage(
            subject=f'New response from {instance.full_name} {instance.email}',
            body=f'U heeft een nieuwe contact aanvraag ontvangen van {instance.full_name}.\n\n',
            to=[settings.DEFAULT_TO_EMAIL],
        ).send()


@receiver(post_save, sender=Feedback)
def send_email_after_feedback_signal(sender, instance: ContactFeedbackModel | Feedback, created, **kwargs):
    """
    Send Email after feedback create
    """
    if created:
        EmailMessage(
            subject=f'New response from {instance.full_name} {instance.email}',
            body=f'U heeft een nieuwe contact aanvraag ontvangen van {instance.full_name}.\n\n',
            to=[settings.DEFAULT_TO_EMAIL],
        ).send()
