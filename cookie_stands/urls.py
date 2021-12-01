from django.urls import path

from .views import StandDetail, StandList

urlpatterns = [
    path("", StandList.as_view(), name="stand_list"),
    path("<int:pk>/", StandDetail.as_view(), name="stand_detail"),
]
