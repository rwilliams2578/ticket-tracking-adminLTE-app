from django.urls import path
from .views import (
    ProjectListView,
    ProjectEditView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectDetailClosedView,
    TicketCreateView,
    TicketEditView,
)

urlpatterns = [
    path(
        "<int:project_pk>/ticket/<int:pk>/edit",
        TicketEditView.as_view(),
        name="ticket_update",
    ),
    path(
        "<int:project_pk>/ticket/new/",
        TicketCreateView.as_view(),
        name="ticket_create",
    ),
    path("<int:pk>/update/", ProjectEditView.as_view(), name="project_update"),
    path(
        "<int:pk>/closed",
        ProjectDetailClosedView.as_view(),
        name="project_detail_closed",
    ),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("new/", ProjectCreateView.as_view(), name="project_create"),
    path("", ProjectListView.as_view(), name="project_list"),
]
