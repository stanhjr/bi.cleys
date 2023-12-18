from apps.website.models.base import (
    CalculatedBlockModel,
    ContactModel,
    FooterModel,
    MetadataModel,
    ReviewsStarsModel,
)
from apps.website.models.category_page import CategoryPage


def category_pages(request):
    return {'category_pages': CategoryPage.objects.prefetch_related('children', 'parent').all()}


def meta(request):
    return {'meta': MetadataModel.objects.last()}


def contacts(request):
    contact_info = ContactModel.objects.last()
    return {'contact_info': contact_info}


def footer(request):
    footer_info = FooterModel.objects.last()
    return {'footer_info': footer_info}


def reviews(request):
    review = ReviewsStarsModel.objects.last()
    return {'reviews': review}


def calculator(request):
    return {'calculator': CalculatedBlockModel.objects.last()}
