from django.urls import path
from . import views

app_name = 'building_site'

urlpatterns = [
    path('building_site/<int:pk>/', views.BuildingSiteView.as_view(), name='site_view'),
]
