from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)
from django.views.generic.base import ContextMixin, TemplateView

from apps.website.forms import ContactFeedbackForm, FeedbackForm
from apps.website.models import (
    AllProjectPageModel,
    CategoryPage,
    PremiumLoansPageModel,
    PrivacyPolicyModel,
)
from apps.website.models.about_us import AboutUsPageModel
from apps.website.models.base import AppointmentModel
from apps.website.models.contact_page import ContactFeedbackModel, ContactPageModel
from apps.website.models.index import IndexPageModel
from apps.website.models.make_appointment import Feedback, MakeAppointmentPageModel
from apps.website.models.single_project import SingleProjectModel
from apps.website.utils import generate_fake_projects


class ContextPageModelMixin(ContextMixin):
    page_model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_model'] = self.page_model.objects.last()
        return context


class ContextSlugPageModelMixin(ContextPageModelMixin):
    page_model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointment_model'] = AppointmentModel.objects.last()
        return context


class IndexView(ContextPageModelMixin, TemplateView):
    template_name = 'pages/index.html'
    page_model = IndexPageModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_home_page'] = True
        context['categories'] = CategoryPage.objects.filter(
            children__isnull=True
        )
        context['projects'] = SingleProjectModel.objects.all()[:10]
        return context


class AboutUsView(ContextPageModelMixin, TemplateView):
    template_name = 'pages/about_us.html'
    page_model = AboutUsPageModel


class PrivacyPolicyView(ContextPageModelMixin, TemplateView):
    template_name = 'pages/privacy_policy.html'
    page_model = PrivacyPolicyModel


class MakeAppointmentView(ContextPageModelMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'pages/make_appointment.html'
    success_url = reverse_lazy('website:index')
    page_model = MakeAppointmentPageModel


class ContactView(ContextPageModelMixin, CreateView):
    model = ContactFeedbackModel
    form_class = ContactFeedbackForm
    template_name = 'pages/contact.html'
    success_url = reverse_lazy('website:index')
    page_model = ContactPageModel


class PremiumLoansPageView(ContextPageModelMixin, TemplateView):
    template_name = 'pages/premies_leningen.html'
    page_model = PremiumLoansPageModel


class CategoryDetailView(DetailView):
    model = CategoryPage
    template_name = 'pages/category_page.html'
    context_object_name = 'page_model'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['appointment_model'] = AppointmentModel.objects.last()
        context['projects'] = SingleProjectModel.objects.filter(related_categories=self.object)
        return self.render_to_response(context)


class SingleProjectDetailView(DetailView):
    model = SingleProjectModel
    template_name = 'pages/single_page.html'
    context_object_name = 'page_model'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['appointment_model'] = AppointmentModel.objects.last()
        context['similar_projects'] = SingleProjectModel.objects.filter(
            related_categories__in=self.object.related_categories.all()
        ).exclude(pk=self.object.pk).distinct()[:3]
        context['booking_split'] = True
        context['result_white'] = True
        return self.render_to_response(context)


class ProjectListView(ContextPageModelMixin, ListView):
    template_name = 'pages/all_projects.html'
    model = SingleProjectModel
    page_model = AllProjectPageModel
    context_object_name = 'projects'
    paginate_by = 17

    def get_queryset(self):
        category_slug = self.request.GET.get('category')
        qs = super().get_queryset().prefetch_related('related_categories', 'preview_images')
        if category_slug:
            return qs.filter(related_categories__slug=category_slug).order_by('created_at')
        return qs.order_by('created_at')

    def get_context_data(self, **kwargs):
        generate_fake_projects()
        context = super().get_context_data(**kwargs)
        projects_count = self.get_queryset().count()
        context['pagination'] = projects_count > self.paginate_by
        context['projects_count'] = projects_count
        context['categories'] = CategoryPage.objects.filter(
            children__isnull=True
        ).prefetch_related('children', 'parent')
        category_slug = self.request.GET.get('category')
        if category_slug:
            context['get_params'] = f'&category={category_slug}'
        return context


def handler404(request, exception):
    response = render(request, '404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response
