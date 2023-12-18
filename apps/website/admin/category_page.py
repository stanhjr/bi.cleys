from django.contrib import admin

from apps.website.models.category_page import (
    AnimationBlock,
    CalculatorBlock,
    CategoryPage,
    CategorySliderModel,
    ContentBlock,
    CTAOptionalBlock,
    ProjectBlock,
    RelatedProjects,
    ResultBlock,
    VideoBlock,
)


class CategorySliderInline(admin.StackedInline):
    model = CategorySliderModel
    extra = 0


class RelatedProjectsInline(admin.StackedInline):
    model = RelatedProjects
    extra = 0


class VideoBlockInline(admin.StackedInline):
    model = VideoBlock
    extra = 0


class AnimationBlockInline(admin.StackedInline):
    model = AnimationBlock
    extra = 0


class ProjectBlockInline(admin.StackedInline):
    model = ProjectBlock
    extra = 0


class ResultBlockInline(admin.StackedInline):
    model = ResultBlock
    extra = 0


class CalculatorBlockInline(admin.StackedInline):
    model = CalculatorBlock
    extra = 0


class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 0


class CTAOptionalBlockInline(admin.StackedInline):
    model = CTAOptionalBlock
    extra = 0


@admin.register(CategoryPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    inlines = [
        CategorySliderInline,
        RelatedProjectsInline,
        AnimationBlockInline,
        ContentBlockInline,
        CalculatorBlockInline,
        VideoBlockInline,
        ProjectBlockInline,
        CTAOptionalBlockInline,
        ResultBlockInline,
    ]
