from django.urls import path

from apps.website.views import (
    AboutUsView,
    CategoryDetailView,
    ContactView,
    CookiesView,
    IndexView,
    MakeAppointmentView,
    PremiumLoansPageView,
    PrivacyPolicyView,
    ProjectListView,
    SingleProjectDetailView,
    TermsAndConditionsView,
)

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('make-appointment/', MakeAppointmentView.as_view(), name='make_appointment'),
    path('contacts/', ContactView.as_view(), name='contact_page'),
    path('premies-leningen/', PremiumLoansPageView.as_view(), name='premium_loans'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('cookie-policy/', CookiesView.as_view(), name='cookies_policy'),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms_policy'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<pk>/', SingleProjectDetailView.as_view(), name='project_single_detail'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category_page_detail'),
]
