from django.urls import path
from . import views
urlpatterns = [
    path('',views.display,name='index'),
    path('1/<int:pk>',views.ar,name='ar'),
    path('2',views.about,name='about')
]