from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name="index"),
   path('Time_series', views.Time_series, name="Time_series"),
   path('Survival_analysis', views.Survival_analysis, name="Survival_analysis")
]