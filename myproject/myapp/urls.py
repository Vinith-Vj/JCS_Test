from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='boat'),
    path('boat', views.boat, name='boat'),
    path('package/<slug:slug>/', views.package, name='package'),
]