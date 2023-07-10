from django.urls import path

from tasks.views import (
    TaskStatusUpdateView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    TagListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    TaskListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path(
        "tasks/<int:pk>/status/",
        TaskStatusUpdateView.as_view(),
        name="task-status-update",
    ),
]

app_name = "tasks"
