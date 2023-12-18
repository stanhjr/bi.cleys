from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from apps.website.models.contact_page import ContactFeedbackModel
from apps.website.models.make_appointment import Feedback, ServicesAppointment


class FeedbackForm(forms.ModelForm):
    appointments = forms.ModelMultipleChoiceField(
        queryset=ServicesAppointment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    recaptcha = ReCaptchaField()

    class Meta:
        model = Feedback
        fields = [
            'full_name', 'email', 'phone', 'message', 'post_code',
            'estimate_facade_area', 'image', 'appointments'
        ]


class ContactFeedbackForm(forms.ModelForm):
    recaptcha = ReCaptchaField()

    class Meta:
        model = ContactFeedbackModel
        fields = [
            'full_name', 'email', 'phone', 'message', 'post_code'
        ]
