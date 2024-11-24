from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("issues/",views.TicketListView.as_view()),
    path("issues/create/",views.TicketCreateView.as_view()),
    path("issues/<int:pk>/",views.TicketSingleView.as_view()),
    path("issues/<int:pk>/modify/",views.TicketDelandUpdate.as_view()),
]
