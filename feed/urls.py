from django.urls import path
from .views import HomePageView

app_name = 'feed'

urlpatterns = [
    path('', RenderSomeView, name='index'),
]