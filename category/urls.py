from django.urls import path

from .views import *

urlpatterns = [
    path("", Category1ListView.as_view(), name="lvl1_listview"),
    path("<int:pk>/", Category1DetailView.as_view(), name="lvl1_detailview"),
]
