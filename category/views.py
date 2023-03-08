from django.views.generic import ListView, DetailView

from .models import CategoryDepth1, CategoryDepth2, CategoryDepth3


class Category1ListView(ListView):
    model = CategoryDepth1
    template_name = "category/category1_list.html"
    context_object_name = "categories"


class Category1DetailView(DetailView):
    model = CategoryDepth1
    template_name = "category/category1_detail.html"
    context_object_name = "category"
