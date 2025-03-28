from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<str:auteur>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<str:auteur>/results/", views.results, name="results")
]