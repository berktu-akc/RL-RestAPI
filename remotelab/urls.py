from django.contrib import admin
from django.urls import path
from remotelab import views

app_name = "remotelab"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('experiments/',views.getACDC,name="experiments"),
    path('experiments/experiment1',views.getExperiment1,name="experiment1"),
    path('experiments/solutions',views.solutions,name="solutions"),
]
