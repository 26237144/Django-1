from django.urls import path
from pages import views
from pages.views import HomePageView

urlpatterns=[

    path("",HomePageView.as_view())
]