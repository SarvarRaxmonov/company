from django.urls import path
from apps.job.views import FilterViewSet

urlpatterns = [
   path("counts/",FilterViewSet.as_view({'get':'get'}), name="counts")
]


