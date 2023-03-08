from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import CategoryDepth1, CategoryDepth2, CategoryDepth3


# class SubCategoryFilter(SimpleListFilter):
#     title = "Has Subcategories"
#     parameter_name = "has_subcategories"

#     def lookups(self, request, model_admin):
#         return (
#             ('has','has subcategories'),
#             ('nohas','no has subcategories'),
#         )

#     def queryset(self, request, queryset):
#         return queryset.filter(

#         )


class Depth2Inline(admin.TabularInline):
    model = CategoryDepth2


@admin.register(CategoryDepth1)
class Lvl1CategoryAdmin(admin.ModelAdmin):
    model = CategoryDepth1
    list_display = (
        "korean_name",
        "english_name",
        "is_esri",
        "code",
    )
    inlines = [
        Depth2Inline,
    ]
    list_filter = ("needs_review",)


class Depth3Inline(admin.TabularInline):
    model = CategoryDepth3


@admin.register(CategoryDepth2)
class Lvl2CategoryAdmin(admin.ModelAdmin):
    model = CategoryDepth2
    list_display = (
        "korean_name",
        "english_name",
        "is_esri",
        "code",
        "depth1",
    )
    inlines = [
        Depth3Inline,
    ]
    list_filter = (
        "depth1__korean_name",
        "needs_review",
    )


@admin.register(CategoryDepth3)
class Lvl3CategoryAdmin(admin.ModelAdmin):
    model = CategoryDepth3
    list_display = (
        "korean_name",
        "english_name",
        "code",
        "depth2",
    )
    list_filter = (
        "depth2__depth1__korean_name",
        # "depth2__korean_name",
        "needs_review",
    )
